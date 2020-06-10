from django.contrib import admin
from .models import Category, MenuItem1, Topping, Sub_Extra

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'price_small', 'price_large']
admin.site.register(MenuItem1, MenuItemAdmin)
admin.site.register(Topping)
admin.site.register(Sub_Extra)
