from django.http import HttpResponse, Http404
from django.shortcuts import render
from itertools import chain
from .models import Category, MenuItem1, Topping, Sub_Extra


# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def about(request):
    return render(request, "orders/about.html")

def menu(request):
    categories = Category.objects.all()
    menulist={}
    for category in categories:
        menulist[category] = MenuItem1.objects.filter(category__name = category)

    context = {
        'categories': categories,
        'menuitems': menulist
    }
    return render(request, "orders/menu.html", context)

def contact(request):
    return render(request, "orders/contact.html")

def cart(request):
    return render(request, "orders/cart.html")


