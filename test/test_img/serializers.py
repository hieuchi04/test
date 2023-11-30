from rest_framework import serializers

from .models import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):

    productimage_set = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ('title', 'description', 'productimage_set')