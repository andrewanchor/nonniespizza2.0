from django.contrib import admin

# Register your models here.
from .models import MENU, Category, Item, Cart, CartItem

admin.site.register(MENU)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)