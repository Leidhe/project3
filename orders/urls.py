from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("menu", views.menu, name="menu"),
    path("cart", views.cart, name="cart"),
    path("product/<int:product_id>", views.product, name="product"),
    path("add_to_cart/<int:item_id>", views.add_to_cart, name="add_to_cart"),


]
