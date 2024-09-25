from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def about_us(request):
    context = {
        'name': 'Muhammad Fadhil Nur Aziz',
        'class': 'PBP A',
        'npm': '2306275531',
    }
    return render(request, 'about_us.html', context)

def create_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)  
        product.user = request.user  
        product.save() 
        return redirect('main:show_products')  

    context = {'form': form}
    return render(request, "create_product.html", context)


@login_required
def show_products(request):
    products = Product.objects.filter(user=request.user)
    context = {'products': products}
    return render(request, 'products.html', context) # Mengarahkan ke template "products.html"

def show_json(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    return HttpResponse(data, content_type='application/json')

def show_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products) 

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:my_account"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:index')

@login_required(login_url='/login')
def my_account(request):
    context = {
        'name': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'my_account.html',context) 
    