from django.urls import path
from .views import add_to_wishlist_view, view_wishlist_view

urlpatterns = [
    path('', view_wishlist_view, name='wishlist-view'),
    path('add/', add_to_wishlist_view, name='wishlist-add'),
]
