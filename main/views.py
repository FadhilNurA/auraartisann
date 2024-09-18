from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product
import json

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
        form.save()
        return redirect('main:show_products')  # Namespace dan nama URL harus sesuai dengan `urls.py`

    context = {'form': form}
    return render(request, "create_product.html", context)


def show_products(request):
    products = Product.objects.all()  # Mengambil semua entri produk dari database
    context = {'products': products}
    return render(request, "products.html", context)  # Mengarahkan ke template "products.html"

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