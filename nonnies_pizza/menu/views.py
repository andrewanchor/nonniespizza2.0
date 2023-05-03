from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Item,Category,MENU, Cart, CartItem
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

def my_view(request):
    context = {'image_path': 'img/my_image.jpg'}
    return render(request, 'my_template.html', context)

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
    context = {'categories': categories,
               'image_path': 'pizza.jpeg'}
    return HttpResponse(template.render(context, request))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request, 'register.html', {'form': form})


@login_required
def cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    total_price = 0
    for item in cart_items:
        total_price += item.item.price * item.quantity
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)

@login_required
def add_to_cart(request, item_id):
    product = Item.objects.get(id=item_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, item=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.cart.user == request.user:
        if cart_item.quantity == 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()
    return redirect('cart')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/') # replace 'home' with the name of your home page URL pattern
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})