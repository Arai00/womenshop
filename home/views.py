from django.shortcuts import render
from cart.models import Product
from clothes.models import Clothing


def home(request):
    amount = len(Product.objects.all())
    clothes = Clothing.objects.filter()[0:5]
    clothess = Clothing.objects.filter()[90:98]
    return render(request, 'index.html', {'amount':amount, 'clothes':clothes, 'clothess':clothess})
