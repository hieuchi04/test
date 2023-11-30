from rest_framework import serializers

from .models import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('product', 'image')


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('title', 'description')