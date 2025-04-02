from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Probuct, Category
from django.contrib import messages

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


def category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        products = Probuct.objects.filter(category=category)
        context = {"category": category, "products": products}
        return render(request, "store/category.html", context)

    except:
        messages.success(request, ("카테고리가 존재 하지 않습니다."))
        return redirect("store:home")
