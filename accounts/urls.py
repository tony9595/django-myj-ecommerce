from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from accounts import views

app_name = "accounts"

urlpatterns = [path("login", views.login_user, name="login_user")]
