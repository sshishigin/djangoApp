from django.contrib import admin
from .models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['company', 'in_box']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
