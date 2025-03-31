from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
]
