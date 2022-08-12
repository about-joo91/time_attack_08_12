from dataclasses import field
from rest_framework import serializers
from .models import Product, UserProduct
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name", "desc", "price"]

class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = "__all__"