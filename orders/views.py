from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Dish, Addition, Order, OrderDish, Topping


# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def about(request):
    return render(request, "orders/about.html")

def menu(request):
    try:
        types = Dish.objects.order_by('type').values_list('type', flat=True).distinct()

        dict_dishes={}

        for type in types:
            dishes = list(Dish.objects.filter(type = type))
            dict_dishes[type]=dishes

    except Dish.DoesNotExist:
        raise Http404("Error")   
    print(dict_dishes)

    return render(request, "orders/menu.html", {'dishes' : dict_dishes})

def contact(request):
    return render(request, "orders/contact.html")

def cart(request):
    return render(request, "orders/cart.html")
