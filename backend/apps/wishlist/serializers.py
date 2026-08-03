from rest_framework import serializers
from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from .models import WishlistItem


class AddToWishlistSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=True
    )


class WishlistItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = WishlistItem
        fields = ('id', 'product', 'created_at')
