from django.urls import path
from .views import add_to_cart_view

urlpatterns = [
    path('add/', add_to_cart_view, name='cart-add'),
]
