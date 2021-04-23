from django.contrib import admin
from .models import Category, Item
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['company', 'in_box']  # The error was there

admin.site.register(Category, CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'title']  # The error was there

admin.site.register(Item, ItemAdmin)