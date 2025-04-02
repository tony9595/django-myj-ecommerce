from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("product/<int:product_id>", views.product, name="product"),
    path("category_summary", views.category_summary, name="category_summary"),
]
