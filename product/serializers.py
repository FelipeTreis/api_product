from rest_framework import serializers

from product.models import Category, Product, Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'name',
            'cnpj',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category',
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'provider',
            'category',
            'input_value',
            'output_value',
        )

    provider = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    output_value = serializers.DecimalField(
        max_digits=7, decimal_places=2, default=None
    )
