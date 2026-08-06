from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction

from apps.cart.models import Cart, CartItem
from .models import Order, OrderItem
from .serializers import OrderHistorySerializer, OrderDetailSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout_view(request):
    # Step 1 — Find the user's cart (get_or_create avoids DoesNotExist)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related('product').all()

    # Step 2 — Reject empty cart immediately, before any transaction
    if not cart_items.exists():
        return Response(
            {
                "success": False,
                "message": "Cart is empty."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # Step 3 — Validate stock for every item before opening a transaction
    for cart_item in cart_items:
        if cart_item.quantity > cart_item.product.stock:
            return Response(
                {
                    "success": False,
                    "message": (
                        f"Insufficient stock for '{cart_item.product.name}'. "
                        f"Requested: {cart_item.quantity}, Available: {cart_item.product.stock}."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    # Step 4 — Everything valid: run checkout as a single atomic operation
    with transaction.atomic():
        # Create Order with a placeholder total; we'll update it after items are processed
        order = Order.objects.create(user=request.user, total_amount=0)

        running_total = 0

        for cart_item in cart_items:
            product = cart_item.product

            # Snapshot: copy price and name at this exact moment
            price_at_purchase = product.price
            product_name = product.name

            # Create the OrderItem with snapshots
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=cart_item.quantity,
                price_at_purchase=price_at_purchase,
                product_name=product_name,
            )

            # Accumulate running total
            running_total += price_at_purchase * cart_item.quantity

            # Reduce stock
            product.stock -= cart_item.quantity
            product.save()

        # Save the final calculated total onto the Order
        order.total_amount = running_total
        order.save()

        # Clear CartItems — keep the Cart row itself (empty cart is valid)
        cart_items.delete()

    return Response(
        {
            "success": True,
            "message": "Order placed successfully.",
            "order_id": order.id
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history_view(request):
    # Always scope to request.user — never expose another user's orders
    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    serializer = OrderHistorySerializer(orders, many=True)
    return Response(
        {
            "success": True,
            "count": orders.count(),
            "orders": serializer.data
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_detail_view(request, order_id):
    # Ownership-scoped lookup — prevents one user viewing another's order
    try:
        order = Order.objects.prefetch_related("items").get(
            id=order_id,
            user=request.user
        )
    except Order.DoesNotExist:
        return Response(
            {
                "success": False,
                "message": "Order not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = OrderDetailSerializer(order)
    return Response(
        {
            "success": True,
            "order": serializer.data
        },
        status=status.HTTP_200_OK
    )
