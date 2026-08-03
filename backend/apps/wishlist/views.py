from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Wishlist, WishlistItem
from .serializers import AddToWishlistSerializer, WishlistItemSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_wishlist_view(request):
    serializer = AddToWishlistSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            {
                "success": False,
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    product = serializer.validated_data['product']

    # Get or create wishlist for authenticated user
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    # Get or create WishlistItem — prevents duplicate rows via unique_together constraint
    item, created = WishlistItem.objects.get_or_create(
        wishlist=wishlist,
        product=product
    )

    if created:
        return Response(
            {
                "success": True,
                "message": "Product added to wishlist.",
                "item": WishlistItemSerializer(item).data
            },
            status=status.HTTP_201_CREATED
        )
    else:
        return Response(
            {
                "success": True,
                "message": "Product already in wishlist.",
                "item": WishlistItemSerializer(item).data
            },
            status=status.HTTP_200_OK
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_wishlist_view(request):
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    items = (
        wishlist.items
        .select_related("product")
        .prefetch_related("product__images")
        .order_by("-created_at")
    )
    serializer = WishlistItemSerializer(items, many=True)
    return Response(
        {
            "success": True,
            "count": items.count(),
            "items": serializer.data
        },
        status=status.HTTP_200_OK
    )
