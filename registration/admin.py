from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active']
    list_display_links = ['id', 'name']
    list_per_page = 20


@admin.register(Ticker)
class TickerAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name', 'code']
    list_display = ['id', 'name', 'code', 'category_id', 'is_active']
    list_display_links = ['id', 'name']
    list_per_page = 20


@admin.register(AssetWallet)
class AssetWalletAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'name', 'is_active']


@admin.register(AssetsInWallet)
class AssetWalletInAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'asset_wallet', 'ticker']
    raw_id_fields = ['ticker']