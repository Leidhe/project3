from django.contrib import admin
from .models import Dish, Addition, Order, OrderDish, Topping

# Register your models here.

admin.site.register(Dish)
admin.site.register(Topping)
admin.site.register(Addition)
admin.site.register(OrderDish)
admin.site.register(Order)
