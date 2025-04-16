from rest_framework import serializers
from store.models import Category, Product


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     price = serializers.ImageField()
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     description = serializers.CharField(
#         max_length=250, required=False, allow_blank=True, allow_null=True
#     )
#     image = serializers.ImageField()
#     is_sale = serializers.BooleanField()
#     sale_price = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["id","name","category"]

    # dev_31
    # 가격은 0 이상 10,000 이하
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("가격은 0 이상으로 설정해주세요.")

        if value > 10000:
            raise serializers.ValidationError("가격은 10만원 이하로 설정해주세요.")
