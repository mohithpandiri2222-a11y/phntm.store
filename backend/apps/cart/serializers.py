from rest_framework import serializers
from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from .models import CartItem


class AddToCartSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=True
    )


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity', 'subtotal')

    def get_subtotal(self, obj):
        return str(round(obj.product.price * obj.quantity, 2))


class CartSerializer(serializers.Serializer):
    count = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    def get_count(self, cart):
        return cart.items.count()

    def get_items(self, cart):
        items = cart.items.select_related('product').prefetch_related('product__images')
        return CartItemSerializer(items, many=True).data

    def get_total(self, cart):
        total = sum(
            item.product.price * item.quantity
            for item in cart.items.select_related('product')
        )
        return '{:.2f}'.format(total)


class UpdateCartItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)
