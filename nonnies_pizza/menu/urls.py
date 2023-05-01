from django.urls import path
from . import views

urlpatterns = [path("", views.landing, name = "landing"),
               path("menu/", views.menu, name = "menu"),
               path("menu/register", views.register, name = "register"),
               

]