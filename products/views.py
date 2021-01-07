from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects
    return render(request, 'products/home.html', { 'products':products })
