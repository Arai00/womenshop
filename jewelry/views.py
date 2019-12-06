from django.shortcuts import render
from django.shortcuts import get_list_or_404
from .models import Jewelry
from cart.models import Product


def jewelry(request):
    jewelry = Jewelry.objects.all()
    amount = len(Product.objects.all())
    return render(request, 'jewel.html', {'jewelries': jewelry, 'amount':amount})


def details(request, pk):
    jewelry = Jewelry.objects.get(pk=pk)
    amount = len(Product.objects.all())
    jewelries = Jewelry.objects.filter()[10:15]
    return render(request, 'detailsJ/details.html', {'jewelry':jewelry, 'jewelries': jewelries, 'amount':amount})