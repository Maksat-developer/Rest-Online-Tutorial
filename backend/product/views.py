from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductSerializer



@api_view(["POST", "GET"])
def api_home(request, *args, **kwargs):
    """
        DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        return Response(serializer.data) 
    return Response("Invslid")
    
     













# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title'])
#     return HttpResponse(data)

























# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data['id'] = model_data.id
#         data['title'] = model_data.title
#         data['content'] = model_data.content
#         data['price'] = model_data.price
#         # model instance (model_data)
#         # turn a Python dict
#         # retutrn JSON to my client

#     return JsonResponse(data)

