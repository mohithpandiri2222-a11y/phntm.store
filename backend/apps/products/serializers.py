from rest_framework import serializers
from .models import Product, Category, ProductImage

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=True
    )
    name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=0, required=True)
    stock = serializers.IntegerField(min_value=0, required=True)

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'description', 'price', 'stock', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'display_order', 'is_primary')
        read_only_fields = ('id', 'image', 'display_order', 'is_primary')


class ProductImageUploadSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    display_order = serializers.IntegerField(default=0, min_value=0, required=False)
    is_primary = serializers.BooleanField(default=False, required=False)

    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'display_order', 'is_primary')
        read_only_fields = ('id',)
