from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import AddToCartSerializer, CartSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart_view(request):
    serializer = AddToCartSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {
                "success": False,
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    product = serializer.validated_data['product']

    # Get the user's cart, or create one if it doesn't exist yet
    cart, _ = Cart.objects.get_or_create(user=request.user)

    # Check if this product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )

    if created:
        return Response(
            {
                "success": True,
                "message": "Product added to cart."
            },
            status=status.HTTP_201_CREATED
        )

    # Product already in cart — increment quantity
    cart_item.quantity += 1
    cart_item.save()
    return Response(
        {
            "success": True,
            "message": "Product quantity updated.",
            "quantity": cart_item.quantity
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    serializer = CartSerializer(cart)
    return Response(
        {
            "success": True,
            **serializer.data
        },
        status=status.HTTP_200_OK
    )
