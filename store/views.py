from django.shortcuts import render
from django.http import HttpResponse
from store.models import Probuct, Category

# Create your views here.


def home(request):
    products = Probuct.objects.all()
    return render(request, "store/home.html", {"products": products})


def about(request):
    return render(request, "store/about.html", {})


def product(request, product_id):
    product = Probuct.objects.get(id=product_id)
    return render(request, "store/product.html", {"product": product})


def category_summary(request):
    categories = Category.objects.all()
    return render(request, "store/category_summary.html", {"categories": categories})
