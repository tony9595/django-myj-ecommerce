from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from api import views

# dev_28
app_name = "api"

urlpatterns = [
    path("hello-world/", views.hello_world),
    path("hello-world-json/", views.hello_world_json),
    path("hello-world-drf/", views.hello_world_drf),
]
