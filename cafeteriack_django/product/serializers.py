from rest_framework import serializers

from .models import Vertical, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "sugar",
            "coffee",
            "flour",
            "chocolate"
        )


class VerticalSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Vertical
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = (
            "thumbnail",
        )
        fields = (
            "name",
            "slug",
            "vertical",
            "sugar",
            "coffee",
            "flour",
            "chocolate",
            "description",
            "price",
            "image",
        )