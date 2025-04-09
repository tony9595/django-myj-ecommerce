from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from cart.cart import Cart
from orders.models import Order, OrderItem
from payment.models import Payment
from store.models import Product

# Create your views here.
@login_required(login_url="accounts:login_user")
def payment_process(request):
    if request.POST:
        cart = Cart(request)
        if 100 == int(request.POST["paid_amount"]):
            user = request.user
            create_order =Order(user=user)
            create_order.amount_paid = cart.get_product_total()
            create_order.save()

            # 주문 생성후 주문번호를 바탕으로 주문 아이템 생성
            order_id = create_order.pk

            for item in cart:
                create_order_item = OrderItem(
                    order_id = order_id,
                    product_id = item['procuct'].id,
                    quantity = item['quantity'],
                    price = item['price']
                )
            
            create_payment = Payment(orde = create_order)
            create_payment.imp_uid = request.POST["imp_uid"]
            create_payment.save()

            cart_keys = list(cart.get_cart().keys())
            for product_id in cart_keys:
                product = Product.objects.get(id=product_id)
                cart.remove(product)

            messages.success(request,"결제가 완료되었습니다.")
            return HttpResponse("SUCCESS")


        else:
            messages.success(request,"결제금액이 맞지 않아 취소 되었습니다")
            return redirect("/")