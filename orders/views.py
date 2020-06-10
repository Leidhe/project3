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

def cart(request):
    return render(request, "orders/cart.html")

def product(request, product_id):
    item = MenuItem1.objects.get(id=product_id)
    print(item)
    if item.category.name == 'Regular Pizza' or  item.category.name == 'Silician Pizza':
        extras = Topping.objects.all()
        title = "Choose your toppings"
    elif item.category.name == 'Subs':
        extras = Sub_Extra.objects.filter(subs__id = item.id)
        title = "Choose any extra"
    else:
        title = None
        extras=[]
    context = {
        'item': item,
        'extras': extras,
        'title': title
    }
    return render(request, "orders/product-single.html", context)

