from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.models import Product
from api.serializers import ProductSerializer


@api_view(["GET", "POST"])
def products_api(request):

    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # 디시리얼라이져
    if request.method == "POST":
        print(request.data)
        print("타입 : ", type(request.data))
        serializer = ProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


@api_view(["GET", "DELETE", "PUT"])
def product_api(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        product.delete()
        return Response("SUCCESS", status=status.HTTP_204_NO_CONTENT)
