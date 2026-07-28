from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

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
