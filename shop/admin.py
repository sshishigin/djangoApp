from django.contrib import admin

from .models import Category, Item, UserItemRelation


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['company', 'in_box']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'price']


class UserItemRelationAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'like']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(UserItemRelation, UserItemRelationAdmin)
