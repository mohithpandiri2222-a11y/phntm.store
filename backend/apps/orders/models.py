from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product

User = get_user_model()

STATUS_CHOICES = [
    ("PENDING", "Pending"),
    ("PROCESSING", "Processing"),
    ("SHIPPED", "Shipped"),
    ("DELIVERED", "Delivered"),
    ("CANCELLED", "Cancelled"),
]


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} — {self.user.username} — {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name="order_items"
    )
    quantity = models.PositiveIntegerField()
    # Snapshot: price captured at checkout — never changes even if Product.price changes later
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    # Snapshot: product name captured at checkout — preserved even if product is renamed
    product_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.quantity}x {self.product_name} in Order #{self.order.id}"
