from django.urls import path
from .views import add_to_cart_view, view_cart_view

urlpatterns = [
    path('', view_cart_view, name='cart-view'),
    path('add/', add_to_cart_view, name='cart-add'),
]
