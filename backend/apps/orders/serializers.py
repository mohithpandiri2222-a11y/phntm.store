from rest_framework import serializers
from .models import Order


class OrderHistorySerializer(serializers.ModelSerializer):
    """
    Lightweight summary serializer for the Order History list.
    Returns only the fields needed for the 'My Orders' screen —
    no nested OrderItems (those belong to the future Order Detail API).
    """
    class Meta:
        model = Order
        fields = ['id', 'total_amount', 'status', 'created_at']
