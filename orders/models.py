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
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="orderitem_user")
    item = models.ForeignKey(MenuItem1, on_delete=models.CASCADE, related_name="orderitem_menuitem1")
    size = models.CharField(max_length=64)
    toppings = models.ManyToManyField(Topping, related_name="orderitem_toppings", blank="True")
    subs_extra = models.ManyToManyField(Sub_Extra, related_name="orderitem_subsextras", blank="True")
    price = models.FloatField(default=0)


    def __str__(self):
        return f"{self.item}"

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    total = models.FloatField(default=0)
    street_address = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    postcode = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_cart")
    item = models.ForeignKey(MenuItem1, on_delete=models.CASCADE, related_name="cartitem_menuitem1")
    size = models.CharField(max_length=64)
    toppings = models.ManyToManyField(Topping, related_name="cartitem_toppings", blank="True")
    subs_extra = models.ManyToManyField(Sub_Extra, related_name="cartitem_subsextras", blank="True")
    price = models.FloatField(default=0)


 
