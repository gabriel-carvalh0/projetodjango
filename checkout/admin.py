from django.contrib import admin

from .models import CartItem, Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CartItem)