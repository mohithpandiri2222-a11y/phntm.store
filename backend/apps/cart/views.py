from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import AddToCartSerializer, CartSerializer, UpdateCartItemSerializer


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


def _update_cart_item_logic(request, item_id):
    # Ownership-scoped lookup — prevents one user modifying another's cart
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
    except CartItem.DoesNotExist:
        return Response(
            {
                "success": False,
                "message": "Cart item not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = UpdateCartItemSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {
                "success": False,
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    cart_item.quantity = serializer.validated_data['quantity']
    cart_item.save()

    from .serializers import CartItemSerializer
    return Response(
        {
            "success": True,
            "message": "Cart item updated successfully.",
            "item": CartItemSerializer(cart_item).data
        },
        status=status.HTTP_200_OK
    )


def _remove_cart_item_logic(request, item_id):
    # Ownership-scoped lookup — prevents one user deleting another's cart item
    try:
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
    except CartItem.DoesNotExist:
        return Response(
            {
                "success": False,
                "message": "Cart item not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )

    cart_item.delete()
    return Response(
        {
            "success": True,
            "message": "Item removed from cart."
        },
        status=status.HTTP_200_OK
    )


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_cart_item_view(request, item_id):
    return _update_cart_item_logic(request, item_id)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart_view(request, item_id):
    return _remove_cart_item_logic(request, item_id)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def cart_item_detail_view(request, item_id):
    if request.method == 'PUT':
        return _update_cart_item_logic(request, item_id)
    elif request.method == 'DELETE':
        return _remove_cart_item_logic(request, item_id)
