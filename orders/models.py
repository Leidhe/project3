from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length = 25)
    size = models.CharField(max_length = 10)
    type = models.CharField(max_length = 25)
    image = models.ImageField(upload_to='images/upload', blank=True)
    price = models.FloatField()
    num_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}. {self.type}. {self.name}, {self.size}, {self.price}, {self.image}'

class Addition(models.Model):
    name = models.CharField(max_length = 25)
    price = models.FloatField()
    dish = models.ManyToManyField(Dish)

    def __str__(self):
        return f'{self.id}. {self.name}, +{self.price}'


class Topping(models.Model):
    name = models.CharField(max_length = 25)

    def __str__(self):
        return f'{self.id}. {self.name}'

class OrderDish(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    additions = models.ManyToManyField(Addition)
    cost = models.FloatField(default=0)

    def __str__(self):
        string = f'Dish {self.dish.name}'
        if self.topping.count > 0:
            string += f'Toppings: '
            for topping in self.toppings.all():
                string += f'{topping.name}'
        if self.additions.count > 0:
            string += f'Additions: '
            for addition in self.additions.all():
                string += f'{addition.name}- +{addition.price}'

        string += f' Price {self.total_price}'
        return string

    def total_price(self):
        total = self.dish.price
        if self.additions.count > 0:
            for addition in self.additions.all():
                total += self.addition.price
        
        return total



class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    order_dishes = models.ManyToManyField(OrderDish)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        string = f' Customer {self.owner}'
        string += f'Dishes:'
        for order_dish in self.order_dishes.all():
            string += f'{order_dish.__str__}:'


    
    


