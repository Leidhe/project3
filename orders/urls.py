from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("menu", views.menu, name="menu"),
    path("cart", views.cart, name="cart"),
    path("product/<int:product_id>", views.product, name="product"),
    path("add_to_cart/<int:item_id>", views.add_to_cart, name="add_to_cart"),
    path("delete_to_cart/<int:item_id>", views.delete_to_cart, name="delete_to_cart"),
    re_path(r"^checkout/(?P<total>\d+\.\d{2})/$", views.checkout, name="checkout"),
    path("place_order", views.place_order, name="place_order"),
    path("orders", views.orders, name="orders"),
    path("view_order/<int:order_id>", views.view_order, name="view_order"),


]
