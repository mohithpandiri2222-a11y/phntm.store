from rest_framework import serializers
from .models import Order, OrderItem, STATUS_CHOICES


class OrderHistorySerializer(serializers.ModelSerializer):
    """
    Lightweight summary serializer for the Order History list.
    Returns only the fields needed for the 'My Orders' screen —
    no nested OrderItems (those belong to the future Order Detail API).
    """
    class Meta:
        model = Order
        fields = ['id', 'total_amount', 'status', 'created_at']


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializes snapshot fields on OrderItem — deliberately avoids nesting
    the live Product object, so deleted products never break order records.
    """
    class Meta:
        model = OrderItem
        fields = ['product_name', 'price_at_purchase', 'quantity']


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    Full order detail: includes all summary fields plus nested OrderItems.
    Used only for GET /api/orders/<id>/ — not the history list.
    """
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'total_amount', 'created_at', 'items']


class UpdateOrderStatusSerializer(serializers.Serializer):
    """
    Input-only serializer for PATCH /api/orders/<id>/status/.
    Validates that the incoming status is one of the allowed STATUS_CHOICES.
    Deliberately separate from OrderDetailSerializer — validation vs. output
    are different responsibilities.
    """
    status = serializers.ChoiceField(choices=[c[0] for c in STATUS_CHOICES])
