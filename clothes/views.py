from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Category, Clothing
from django.db.models import Q
from jewelry.models import Jewelry
from cart.models import Product


def show(request, pk):
    try:
        cloth = Clothing.objects.get(pk=pk)
        clothes = Clothing.objects.filter()[65:70]
        amount = len(Product.objects.all())
        return render(request, 'detailsC/details.html', {'cloth':cloth, 'clothes':clothes, 'amount':amount})
    except:
         return redirect('home')

def clothes(request):
    clothes = Clothing.objects.all()
    amount = len(Product.objects.all())
    return render(request, 'clothing.html', {'clothes':clothes, 'amount':amount})



def category(request, category):
    amount = len(Product.objects.all())
    clothes = Clothing.objects.filter(category__name=category)
    return render(request, 'clothing.html', {'clothes':clothes, 'amount':amount})


def search(request):
    amount = len(Product.objects.all())
    searching = request.GET.get('search', '')
    if searching:
        clothes = Clothing.objects.filter(Q(name__icontains=searching) | Q(category__name__icontains=searching))
        jewelry = Jewelry.objects.filter(name__icontains=searching)
        return render(request, 'searchpage.html', {'jewelry':jewelry, 'clothes':clothes, 'amount':amount})
    else:
        return redirect("/")

# Create your views here.

