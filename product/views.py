from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Category, Product, Provider
from product.serializers import (CategorySerializer, ProductSerializer,
                                 ProviderSerializer)


@api_view()
def providers(request):
    queryset = Provider.objects.all()
    serializer = ProviderSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def categorys(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)
