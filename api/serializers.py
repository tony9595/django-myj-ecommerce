from rest_framework import serializers
from store.models import Category


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    price = serializers.ImageField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objcet.all())
    description = serializers.CharField(
        max_length=250, required=False, allow_blank=True, allow_null=True
    )
    created_at = serializers.DateField()
    updated_at = serializers.DateField()
    is_sale = serializers.BooleanField()
    sale_price = serializers.IntegerField()

