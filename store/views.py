from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "store/home.html", {})
    # return HttpResponse("<h1>개발페이지</h1>")
