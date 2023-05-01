from django.contrib import admin

# Register your models here.
from .models import MENU, Category, Item

admin.site.register(MENU)
admin.site.register(Category)
admin.site.register(Item)