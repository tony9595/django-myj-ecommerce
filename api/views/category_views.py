from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.catagory_serializers import (
    CategorySerializer,
    CategorySimpleSerializer,
)
from store.models import Category


@api_view(["GET"])
def categories_api(request):

    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


# dev_35
class CategoriesAPI(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySimpleSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def put(self, request):
        pass

    def delete(self, request):
        pass


@api_view(["GET"])
def categories_api(request):

    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


# dev_35
class CategoryAPI(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category.delete()
        return Response("삭제 성공", status=status.HTTP_204_NO_CONTENT)


# dev_36
# GenericAPIView : self.get_queryset() 과 sel.get_serializer()를 제공
# ListmodelMixin: self.list() 내부에서 위의 메서드들을 호출
# 주의
# 기본적으로는 quertset, serializer_class 는 약속된 이름
# 대신 커스터마이징은 가능


class CategoriesMixins(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryMixins(RetrieveModelMixin, UpdateModelMixin , DestroyModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySimpleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
