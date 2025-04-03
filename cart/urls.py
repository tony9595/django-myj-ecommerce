from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from cart import views


app_name="cart"

urlpatterns = [
    path("add/",views.add_cart, name="add_cart"),
]
