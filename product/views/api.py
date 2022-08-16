from product.models import Category, Product, Provider
from product.serializers import (CategorySerializer, ProductSerializer,
                                 ProviderSerializer)
from rest_framework.viewsets import ModelViewSet


class ProviderApiViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class CategoryApiViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductApiViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
