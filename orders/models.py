from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"
    
class MenuItem1(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menuitem1_category")
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(max_digits=10, decimal_places=2, blank = True, null=True)
    price_large = models.DecimalField(max_digits=10, decimal_places=2, blank = True, null=True)
    image = models.ImageField(upload_to ='images/upload', default= 'images/no-cameras.png') 
    num_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} -{self.category}"    

class Topping(models.Model):
    name = models.CharField("Topping",max_length=25)

    def __str__(self):
        return f"{self.name}"

class Sub_Extra(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subs = models.ManyToManyField(MenuItem1, related_name="subsextras")

    def __str__(self):
        return f"{self.name}"

class OrderItem(models.Model):
    item = models.ForeignKey(MenuItem1, on_delete=models.CASCADE, related_name="orderitem_menuitem1")
    toppings = models.ManyToManyField(Topping)
    subs_extra = models.ManyToManyField(Sub_Extra)

    def __str__(self):
        return f"{self.item}"

