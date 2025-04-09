
from django import forms
from orders.models import ShippingAddress

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = "__all__"
        exclude = ["user"]