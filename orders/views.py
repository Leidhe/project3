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
        menulist = {}
        for category in categories:
            menulist[category] = MenuItem1.objects.filter(
                category__name=category)

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
            if item.category.name == 'Regular Pizza' or item.category.name == 'Sicilian Pizza':
                if item.num_toppings > 0:
                    extras = Topping.objects.all()
                    title = "Choose your toppings"
                else:
                    title = None
                    extras = []

            elif item.category.name == 'Subs':
                extras = Sub_Extra.objects.filter(subs__id=item.id)
                title = "Choose any extra"
            else:
                title = None
                extras = []

        except KeyError:
            # arreglar
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
    if request.method == "POST" and request.user.is_authenticated:
        menuitem = MenuItem1.objects.get(pk=item_id)
        size = request.POST.get("select-size")
        toppings = request.POST.getlist("checkbox-topping")
        extras = request.POST.getlist("checkbox-subs")

        if len(toppings) > menuitem.num_toppings:
            context = {
                'error': "An error has occured",
            }
            return render(request, "orders/error.html", context)

        try:
            cart_item = CartItem.objects.create(
                user=request.user, item=menuitem, size=size)
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
            return HttpResponseRedirect(reverse('cart'))

        except Exception:
            cart_item.delete()
            context = {
                'error': "An error has occured",
            }
            return render(request, "orders/error.html", context)

    context = {
        'error': "An error has occured",
    }
    return render(request, "orders/error.html", context)


def delete_to_cart(request, item_id):
    if request.method == "POST" and request.user.is_authenticated:
        try:
            item = CartItem.objects.get(user=request.user, pk=item_id)
            item.delete()
        except CartItem.DoesNotExist:
            context = {
                'error': "CartItem not found",
            }
            return render(request, "orders/error.html", context)
        return HttpResponseRedirect(reverse('cart'))
    context = {
        'error': "An error has ocurred",
    }
    return render(request, "orders/error.html", context)


def cart(request):
    if request.user.is_authenticated:

        cartitem_list = CartItem.objects.filter(user=request.user).all()
        total = 0
        for cartitem in cartitem_list:
            total += cartitem.price

        total = Decimal(total)
        total = round(total, 2)
        context = {
            'cartitem_list': cartitem_list,
            'total': total
        }
        return render(request, "orders/cart.html", context)
    return HttpResponseRedirect('/login')


def checkout(request, total):
    if request.method == "POST" and request.user.is_authenticated:
        context = {
            'total': total
        }
        return render(request, "orders/checkout.html", context)

    context = {
        'error': "An error has ocurred",
    }
    return render(request, "orders/error.html", context)


def place_order(request):
    if request.method == "POST" and request.user.is_authenticated:

        street_address = request.POST.get("street_address")
        city = request.POST.get("city")
        postcode = request.POST.get("postcode")
        phone_number = request.POST.get("phone")

        cart_list = CartItem.objects.filter(user=request.user)
        total = 0
        for cart_item in cart_list:
            total += cart_item.price

        try:
            order = Order.objects.create(
                user=request.user,
                total=total,
                street_address=street_address,
                city=city,
                postcode=postcode,
                phone_number=phone_number
            )

            if cart_list:
                for cart_item in cart_list:
                    orderitem = OrderItem.objects.create(
                        user=request.user,
                        item=cart_item.item,
                        size=cart_item.size,
                        price=cart_item.price
                    )
                    for topping in cart_item.toppings.all():
                        orderitem.toppings.add(topping)
                    for sub_extra in cart_item.subs_extra.all():
                        orderitem.subs_extra.add(sub_extra)

                    order.items.add(orderitem)
                cart_list.delete()
            return HttpResponseRedirect('/orders')
        except Exception as e:
            print(e)
            order.delete()
            context = {
                'error': "An error has ocurred",
            }
        return render(request, "orders/error.html", context)
    print("aqui")
    context = {
        'error': "An error has ocurred",
    }
    return render(request, "orders/error.html", context)


def orders(request):
    if request.method == "GET" and request.user.is_authenticated:

        order_list = Order.objects.filter(user=request.user)

        context = {
            'order_list': order_list,
        }
        return render(request, "orders/order_list.html", context)

    context = {
        'error': "An error has ocurred",
    }
    return render(request, "orders/error.html", context)


def view_order(request, order_id):
    if request.user.is_authenticated and request.method == "GET":
        try:
            order = Order.objects.get(id=order_id)
            context = {
                "order": order
            }
            return render(request, "orders/single_order.html", context)
        except Exception as e:
            print(e)
            context = {
                'error': "Order not found",
            }
            return render(request, "orders/error.html", context)
    context = {
        'error': "An error has ocurred",
    }
    return render(request, "orders/error.html", context)

