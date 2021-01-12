from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Vote
from django.utils import timezone

def home(request):
    products = Product.objects
    return render(request, 'products/home.html', { 'products':products })

@login_required(login_url="/account/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.FILES['icon'] and request.POST['body'] and request.FILES['picture'] and request.POST['url']:
            product = Product()
            product.title = request.POST['title']
            product.icon = request.FILES['icon']
            product.body = request.POST['body']
            product.picture = request.FILES['picture']
            product.url = request.POST['url']
            if product.url.startswith("http://") or product.url.startswith("https://"):
                pass
            else:
                product.url = "http://{}".format(product.url)
            product.pub_date = timezone.datetime.now()

            product.hunter = request.user
            product.save()
            vote = Vote(user=request.user, product=Product(product.id))
            vote.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'info':'Please fill all fields'})
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product':product})

@login_required(login_url="/account/signup")
def upvote(request, product_id):
    if request.method=='POST':
        product = get_object_or_404(Product, pk=product_id)
        try:
            vote = Vote.objects.get(user = request.user, product = product_id)
        except:
            vote = None
        if vote == None:
            product.votes_total += 1
            product.save()
            vote = Vote(user=request.user, product=Product(product_id))
            vote.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/detail.html', {'product':product, 'info': 'You voted on this product already'})








