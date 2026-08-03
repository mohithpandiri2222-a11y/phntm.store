from django.urls import path
from .views import add_to_cart_view, view_cart_view, update_cart_item_view

urlpatterns = [
    path('', view_cart_view, name='cart-view'),
    path('add/', add_to_cart_view, name='cart-add'),
    path('items/<int:item_id>/', update_cart_item_view, name='cart-item-update'),
]
