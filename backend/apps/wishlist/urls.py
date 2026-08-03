from django.urls import path
from .views import add_to_wishlist_view

urlpatterns = [
    path('add/', add_to_wishlist_view, name='wishlist-add'),
]
