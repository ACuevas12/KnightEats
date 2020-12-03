from django.contrib import admin
from django.conf import settings

from .models import Order, Item, ItemMenu, ItemCategory, Simple


class ShowOrder(admin.TabularInline):
    model: Order


class ShowItems(admin.TabularInline):
    model: Item


class ShowMenu(admin.TabularInline):
    model: ItemMenu


class ShowCategories(admin.StackedInline):
    model: ItemCategory


class ShowInteger(admin.StackedInline):
    model: Simple


admin.site.register(Order)
admin.site.register(Item)
admin.site.register(ItemMenu)
admin.site.register(ItemCategory)
admin.site.register(Simple)

