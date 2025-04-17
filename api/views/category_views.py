from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers.catagory_serializers import CategorySerializer
from store.models import Category


@api_view(["GET"])
def categories_api(request):

    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
