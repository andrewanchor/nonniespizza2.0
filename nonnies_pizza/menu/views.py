from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Item,Category,MENU

def menu(request):
    categories = Category.objects.prefetch_related('items').all()
    template = loader.get_template('menu.html')
    myitems = Item.objects.all().values()

    context = {
        'myitems': myitems,
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

def landing(request):
    categories = Category.objects.prefetch_related('items').all()
    template = loader.get_template('landing.html')
    context = {'categories': categories}
    return HttpResponse(template.render(context, request))