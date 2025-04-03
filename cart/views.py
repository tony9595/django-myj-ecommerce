from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from cart.cart import Cart
from store.models import Probuct


# Create your views here.
def add_cart(request):
    cart = Cart(request)

    print("카트===", cart)

    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        print("Product_id", product_id)

        product_qty = int(request.POST.get("product_qty"))
        print("Product_qty", product_qty)

        product = get_object_or_404(product, id=product_id)

        cart.add(product, product_qty)

        return JsonResponse({"상품": product_id})
