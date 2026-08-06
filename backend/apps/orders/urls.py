from django.urls import path
from .views import checkout_view, order_history_view, order_detail_view

urlpatterns = [
    path('', order_history_view, name='orders-history'),
    path('checkout/', checkout_view, name='orders-checkout'),
    path('<int:order_id>/', order_detail_view, name='orders-detail'),
]
