from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone



def home(request):
    products = Product.objects
    return render(request, 'products/home.html', { 'products':products })

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.FILES['icon'] and request.POST['body'] and request.FILES['picture'] and request.POST['url']:
            product = Product()
            product.title = request.POST['title']
            product.icon = request.FILES['icon']
            product.body = request.POST['body']
            product.picture = request.FILES['picture']
            product.url = request.POST['url']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('home')
        else:
            return render(request, 'products/create.html', {'info':'Please fill all fields'})
    else:
        return render(request, 'products/create.html')
