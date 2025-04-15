import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def hello_world(request):
    response_date = {}
    response_date["hello"] = "hello"
    response_date["world"] = "world"

    return HttpResponse(json.dumps(response_date))


def hello_world_json(request):
    response_date = {}
    response_date["hello"] = "hello"
    response_date["world"] = "world"

    return JsonResponse(response_date, status=200)


@api_view(["GET"])
def hello_world_drf(request):
    return Response({"message":"Hello World!"})
