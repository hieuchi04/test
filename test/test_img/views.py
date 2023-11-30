from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.

class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all().prefetch_related('productimage_set')
        serializers = ProductSerializer(product, many=True)
        return Response(data=serializers.data)