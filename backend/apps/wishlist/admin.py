from django.contrib import admin
from .models import Wishlist, WishlistItem


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'wishlist', 'product', 'created_at')
    search_fields = ('wishlist__user__username', 'product__name')
    readonly_fields = ('created_at',)
    list_filter = ('created_at',)
