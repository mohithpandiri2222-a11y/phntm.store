from django.urls import path
from .views import add_to_wishlist_view, view_wishlist_view, remove_from_wishlist_view

urlpatterns = [
    path('', view_wishlist_view, name='wishlist-view'),
    path('add/', add_to_wishlist_view, name='wishlist-add'),
    path('items/<int:item_id>/', remove_from_wishlist_view, name='wishlist-remove'),
]
