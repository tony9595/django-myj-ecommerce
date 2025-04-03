from django.conf import settings


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID]

        self.cart = cart

    def __len__(self):
        pass

    def add(self, Product, quantity=1, is_update=False):
        Product_id = str(Product.id)

        if Product_id not in self.cart:
            self.cart[Product_id] = {"quantity": 0, "price": str(Product.price)}

        if is_update:
            self.cart[Product_id]["quantity"] = quantity

        else:
            self.cart[Product_id]["quantity"] += quantity

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
