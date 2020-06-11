from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from itertools import chain
from django.contrib.auth import authenticate
from .models import Category, MenuItem1, Topping, Sub_Extra, Order, OrderItem, CartItem
from decimal import Decimal



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
    if request.method == "POST":
        if request.user.is_authenticated:
            menuitem = MenuItem1.objects.get(pk = item_id)
            size = request.POST.get("select-size")
            toppings = request.POST.getlist("checkbox-topping")
            extras = request.POST.getlist("checkbox-subs")
            

            if len(toppings) > menuitem.num_toppings:
                context = {
                    'error': "An error has occured",
                }
                return render(request, "orders/error.html", context)


            try:
                cart_item = CartItem.objects.create(user=request.user, item=menuitem, size=size)
                if size == 'Small':
                    final_price = menuitem.price_small
                elif size == 'Large':
                    final_price = menuitem.price_large
                else: 
                    if menuitem.price_small:
                        final_price = menuitem.price_small
                    else:
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

                if final_price <= 0:
                    return render(request, "orders/error.html", context)

                cart_item.price = final_price

                cart_item.save()

            except Exception:
                cart_item.delete()
                context = {
                    'error': "An error has occured",
                }
                return render(request, "orders/error.html", context)

            return HttpResponseRedirect(reverse('cart'))
        else:
            return HttpResponseRedirect(reverse('login'))


    context = {
                'error': "Method not allowed",
            }

    return render(request, "orders/error.html", context)


def cart(request):
    cartitem_list = CartItem.objects.filter(user = request.user).all()
    total = 0
    for cartitem in cartitem_list:
        total += cartitem.price

    total = Decimal(total)
    total = round(total,2)
    context={
        'cartitem_list': cartitem_list,
        'total': total
    }
    return render(request, "orders/cart.html", context)


