from rest_framework import serializers
from .models import Product, Category

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
        fields = ('id', 'category', 'name', 'description', 'price', 'stock', 'image', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
