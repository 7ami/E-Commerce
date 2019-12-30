from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Checkout
from math import ceil


def home(request):
    return render(request, 'shop/home.html')


def index(request):
    everyprod = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prods = Product.objects.filter(category=cat)
        n = len(prods)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        everyprod.append([prods, range(1, nSlides), nSlides])

    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # everyprod = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    params = {'allProds': everyprod}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        mess = request.POST.get('mess', '')
        print(name, email, phone, mess)
        contact = Contact(name=name, email=email, phone=phone, mess=mess)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return HttpResponse("I am search")


def productview(request, myid):
    # django automatically takes id iff nott mentioned primary key
    product = Product.objects.filter(id=myid)

    return render(request, 'shop/ProductView.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        itemsjson = request.POST.get('itemsjson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        phone = request.POST.get('phone', '')
        print(name, email, phone, address, address2, city)
        checkout = Checkout(itemsjson=itemsjson, name=name, email=email, address=address, address2=address2,
                            city=city, phone=phone)
        checkout.save()
        thank = True
        id = checkout.check_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')
