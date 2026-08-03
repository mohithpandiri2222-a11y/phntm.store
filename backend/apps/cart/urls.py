from django.urls import path
from .views import (
    add_to_cart_view,
    view_cart_view,
    update_cart_item_view,
    remove_from_cart_view,
    cart_item_detail_view,
)

urlpatterns = [
    path('', view_cart_view, name='cart-view'),
    path('add/', add_to_cart_view, name='cart-add'),
    path('items/<int:item_id>/', cart_item_detail_view, name='cart-item-detail'),
    path('items/<int:item_id>/delete/', remove_from_cart_view, name='cart-item-delete'),
]
