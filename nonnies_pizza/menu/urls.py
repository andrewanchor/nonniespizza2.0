from django.urls import path
from . import views

urlpatterns = [path("", views.landing, name = "landing"),
               path("menu/", views.menu, name = "menu"),
               path("menu/register", views.register, name = "register"),
               path("menu/cart", views.cart, name = "cart"),
               path("add-to-cart/<int:item_id>/", views.add_to_cart, name="add_to_cart"),
               

]