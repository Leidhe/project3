from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, get_list_or_404
from itertools import chain
from django.contrib.auth import authenticate
from .models import Category, MenuItem1, Topping, Sub_Extra, Order, OrderItem, CartItem


# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def about(request):
    return render(request, "orders/about.html")

def menu(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        menulist={}
        for category in categories:
            menulist[category] = MenuItem1.objects.filter(category__name = category)

        context = {
            'categories': categories,
            'menuitems': menulist
        }
        return render(request, "orders/menu.html", context)
    return HttpResponseRedirect('/login')

def cart(request):
    return render(request, "orders/cart.html")

def product(request, product_id):
    if request.user.is_authenticated:
        try:
            item = MenuItem1.objects.get(id=product_id)
            if item.category.name == 'Regular Pizza' or  item.category.name == 'Sicilian Pizza':
                if item.num_toppings > 0:
                    extras = Topping.objects.all()
                    title = "Choose your toppings"
                else: 
                    title = None
                    extras=[]

            elif item.category.name == 'Subs':
                extras = Sub_Extra.objects.filter(subs__id = item.id)
                title = "Choose any extra"
            else:
                title = None
                extras=[]

        except KeyError:
            #arreglar
            return render(request, "product/'product_id'", {"message": "No selection."})
        except MenuItem1.DoesNotExist:
            raise Http404("Menu Item does not exist")

        context = {
            'item': item,
            'extras': extras,
            'title': title
        }
        return render(request, "orders/product-single.html", context)
    return HttpResponseRedirect('/login')

def add_to_cart(request, item_id):
    menuitem = MenuItem1.objects.get(pk = item_id)
    size = request.POST.get("select-size")
    toppings = request.POST.getlist("checkbox-topping")
    extras = request.POST.getlist("checkbox-subs")

    print(menuitem)
    print(size)
    print(type(size))
    print(toppings)
    print(extras)

    try:
        cart_item = CartItem.objects.create(user=request.user, item=menuitem, size=size)
        print(cart_item)
        if size == 'Small':
            final_price = menuitem.price_small
        elif size == 'Large':
            final_price = menuitem.price_large
        if toppings:
            for topping in toppings:
                final = Topping.objects.get(name=topping)
                print(final)
                cart_item.toppings.add(final)
        if extras:
            print("hola")
            for extra in extras:
                final = Sub_Extra.objects.get(name=extra)
                final_price += final.price
                cart_item.subs_extra.add(final)

        cart_item.price = final_price
        cart_item.save()

    except Exception as e:
        cart_item.delete()
        print(type(e))

    return HttpResponseNotFound('<h1>Page not found</h1>')

    


