from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Item,Category,MENU
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})