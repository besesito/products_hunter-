from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from products.models import Product

def signup(request):
    if request.method == 'POST':
        #USER WANTS TO SIGN UP NOW
        if len(request.POST['password2']) > 0 and len(request.POST['password1']) > 0 and len(request.POST['username']) > 0:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    User.objects.get(username=request.POST['username'])
                    return render(request, 'account/signup.html', {'info':"Your user name has been taken, choose diffrent"})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], "", request.POST['password2'])
                    auth.login(request, user)
                    return render(request, 'products/home.html', {'info': "Congratulations {}, You are logged in".format(request.POST['username'])})

            else:
                return render(request, 'account/signup.html', {'info': "Your passwords aren't the same"})
        else:
            return render(request, 'account/signup.html', {'info': "Please fill all fields"})
    else:
        #USER WANTS TO ENTER INFO
        return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            products = Product.objects
            return render(request, 'products/home.html', {'info': "Welcome back {}".format(request.POST['username'].capitalize()), 'products':products})
        else:
            return render(request, 'account/login.html', {'info': "Your login or password is incorrect"})
    else:
        # USER WANTS TO ENTER INFO
        return render(request, 'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        products = Product.objects
        return render(request, 'products/home.html', {'info': "You are logged out", 'products':products})
