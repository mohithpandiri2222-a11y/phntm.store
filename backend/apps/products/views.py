from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer, ProductImageUploadSerializer

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_product_view(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "success": True,
                "message": "Product created successfully.",
                "product": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(
        {
            "success": False,
            "errors": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
@permission_classes([AllowAny])
def list_products_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(
        {
            "success": True,
            "count": products.count(),
            "products": serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([AllowAny])
def retrieve_product_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(
            {
                "success": False,
                "message": "Product not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = ProductSerializer(product)
    return Response(
        {
            "success": True,
            "product": serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_product_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(
            {
                "success": False,
                "message": "Product not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "success": True,
                "message": "Product updated successfully.",
                "product": serializer.data
            },
            status=status.HTTP_200_OK
        )
    return Response(
        {
            "success": False,
            "errors": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(
            {
                "success": False,
                "message": "Product not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )
    product.delete()
    return Response(
        {
            "success": True,
            "message": "Product deleted successfully."
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET', 'POST'])
def product_images_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(
            {
                "success": False,
                "message": "Product not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )

    # GET — list all images (public)
    if request.method == 'GET':
        images = product.images.all().order_by('display_order')
        serializer = ProductImageSerializer(images, many=True)
        return Response(
            {
                "success": True,
                "count": images.count(),
                "images": serializer.data
            },
            status=status.HTTP_200_OK
        )

    # POST — upload a new image (admin only)
    if not request.user or not request.user.is_authenticated or not request.user.is_staff:
        return Response(
            {"detail": "Authentication credentials were not provided."}
            if not request.user or not request.user.is_authenticated
            else {"detail": "You do not have permission to perform this action."},
            status=status.HTTP_401_UNAUTHORIZED
            if not request.user or not request.user.is_authenticated
            else status.HTTP_403_FORBIDDEN
        )

    serializer = ProductImageUploadSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.validated_data.get('is_primary', False):
            ProductImage.objects.filter(product=product, is_primary=True).update(is_primary=False)
        image_instance = serializer.save(product=product)
        read_serializer = ProductImageSerializer(image_instance)
        return Response(
            {
                "success": True,
                "message": "Product image uploaded successfully.",
                "image": read_serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(
        {
            "success": False,
            "errors": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product_image_view(request, image_id):
    try:
        image = ProductImage.objects.get(id=image_id)
    except ProductImage.DoesNotExist:
        return Response(
            {
                "success": False,
                "message": "Image not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )
    image.delete()
    return Response(
        {
            "success": True,
            "message": "Product image deleted successfully."
        },
        status=status.HTTP_200_OK
    )
