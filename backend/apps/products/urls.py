from django.urls import path
from .views import create_product_view, list_products_view, retrieve_product_view, update_product_view, delete_product_view

urlpatterns = [
    path('', create_product_view, name='product-create'),
    path('list/', list_products_view, name='product-list'),
    path('<int:pk>/', retrieve_product_view, name='product-detail'),
    path('<int:pk>/update/', update_product_view, name='product-update'),
    path('<int:pk>/delete/', delete_product_view, name='product-delete'),
]
