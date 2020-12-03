from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    # basically, many orders fit into a single profile

    order_num = models.IntegerField(primary_key=True, unique=True)
    order_time = models.DateTimeField(default=datetime.now(), blank=True)
    order_finished = models.BooleanField(default=False)
    order_paid = models.BooleanField(default=False)
    order_archived = models.BooleanField(default=False)
    order_total = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.user.username) + " : " + str(self.order_num)


class ItemMenu(models.Model):
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_changed = models.DateTimeField(default=datetime.now(), blank=True)
    menu_name = models.CharField(max_length=200, default="")

    def __str__(self):
        return str(self.menu_name)


class ItemCategory(models.Model):
    category_name = models.CharField(max_length=200, default="", null=True)

    def __str__(self):
        return str(self.category_name)


class Item(models.Model):
    on_order = models.ForeignKey(Order, on_delete=models.CASCADE, default='')  # changed from manytomany to foreignkey
    on_menu = models.ForeignKey(ItemMenu, on_delete=models.CASCADE, default='')  # belongs on menu or inactive
    on_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, default='')  # what category is this

    item_name = models.CharField(max_length=200, default='')
    item_quantity = models.IntegerField(default=1)
    item_price = models.FloatField(default=1.0)

    def __str__(self):
        return str(self.item_name) + "  Qty: " + str(self.on_order)


class Simple(models.Model):
    simple_integer = models.IntegerField(default=1)

    def __str__(self):
        return str(self.simple_integer)
