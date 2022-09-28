from product.models import Category, Product, Provider
from product.serializers import (CategorySerializer, ProductSerializer,
                                 ProviderSerializer)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet


class Pagiantion(PageNumberPagination):
    page_size = 10


class ProviderApiViewSet(ModelViewSet):
    queryset = Provider.objects.filter(is_active=True)
    serializer_class = ProviderSerializer
    pagination_class = Pagiantion
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class CategoryApiViewSet(ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    pagination_class = Pagiantion
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class ProductApiViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    pagination_class = Pagiantion
    permission_classes = [IsAuthenticatedOrReadOnly, ]
