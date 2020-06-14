from django.contrib import admin
from .models import Category, MenuItem1, Topping, Sub_Extra, Order, OrderItem, CartItem

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'price_small', 'price_large']

class Subs_ExtraAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']    

class ToppingsAdmin(admin.ModelAdmin):
    list_display = ['name']  

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['user', 'total', 'created_on']  

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'size', 'price']  

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'size', 'price'] 


admin.site.register(MenuItem1, MenuItemAdmin)
admin.site.register(Topping, ToppingsAdmin)
admin.site.register(Sub_Extra, Subs_ExtraAdmin)
admin.site.register(Order, OrdersAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(CartItem, CartItemAdmin)

