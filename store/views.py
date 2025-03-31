from django.shortcuts import render
from django.http import HttpResponse
from store.models import Probuct

# Create your views here.


def home(request):
    products = Probuct.objects.all()
    return render(request, "store/home.html", {"products": products})


def about(request):
    return render(request, "store/about.html")
