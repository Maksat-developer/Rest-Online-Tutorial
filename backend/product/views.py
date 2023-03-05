from rest_framework import generics
from rest_framework.response import Response



from .serializers import ProductSerializer
from .models import Product



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    