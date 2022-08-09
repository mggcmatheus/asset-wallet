from django.contrib import admin
from .models import Category, Ticker


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active']
    list_display_links = ['id', 'name']
    list_per_page = 20


@admin.register(Ticker)
class TickerAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'code', 'category_id', 'is_active']
    list_display_links = ['id', 'name']
    list_per_page = 20
