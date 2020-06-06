from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def about(request):
    return render(request, "orders/about.html")

def menu(request):
    return render(request, "orders/menu.html")

def contact(request):
    return render(request, "orders/contact.html")

def cart(request):
    return render(request, "orders/cart.html")