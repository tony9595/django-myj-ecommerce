from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from api.views import hello_world_drf,hello_world,hello_world_json
from .views import base_views, product_views, category_views


# dev_28
app_name = "api"

urlpatterns = [
    # path("hello-world/", base_views.hello_world),
    # path("hello-world-json/", base_views.hello_world_json),
    # path("hello-world-drf/", base_views.hello_world_drf),
    # dev_29
    # 방식     url           기능
    # GET    products/       list
    # POST   products/       create
    # GET    product/{id}    create
    # PUT    product/{id}   modify product
    # DELETE product/{id}   delete product
    path("products/", product_views.products_api),
    path("product/<int:pk>/", product_views.product_api),
    # dev_32
    # dev_35
    # 방식   url                  기능
    # GET  categories/            list
    # POST categories/            create
    # Get  categories/{id}         product
    # PUT  categories/{id}       modify product
    # DELETE  categories/{id}    delete product
    # path("categories/", category_views.CategoriesAPI.as_view()),
    # path("category/<int:pk>/", category_views.CategoryAPI.as_view()),
    # dev_36
    path("categories/", category_views.CategoriesMixins.as_view()),
    path("category/<int:pk>/", category_views.CategoryMixins.as_view()),
]
