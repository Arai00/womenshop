from django.shortcuts import render, redirect
from clothes.models import Clothing
from jewelry.models import Jewelry
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def cartClothes(request, pk):
    clothes = Clothing.objects.get(pk=pk)
    try:
        cart = Product.objects.get(name=clothes.name)
        cart.quantity+=1
        cart.price+=cart.price
        cart.save()
        return redirect("cartshow")
    except:
        cart = Product(name=clothes.name, image=clothes.image, price= clothes.price)
        cart.save()
        return redirect("cartshow")

@login_required(login_url='login')
def cartJew(request, pk):
    jewerly = Jewelry.objects.get(pk=pk)
    try:
        jew = Product.objects.get(name=jewerly.name)
        jew.quantity += 1
        jew.price += jew.quantity
        jew.save()
        return redirect("cartshow")
    except:
        jew = Product(name=jewerly.name, image=jewerly.image, price=jewerly.price)
        jew.save()
        return redirect("cartshow")

@login_required(login_url='login')
def cartshow(request):
    total = 0
    cart = Product.objects.all()
    clothes = Clothing.objects.filter()[16:20]
    for cartt in cart:
        total += cartt.price
    return render(request, 'cart.html', {'carts':cart, 'total':total, 'clothes':clothes})

@login_required(login_url='login')
def delete(request):
    Product.objects.all().delete()
    return redirect('home')

# Create your views here.
