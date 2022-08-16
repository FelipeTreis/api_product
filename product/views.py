from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Category, Product, Provider
from product.serializers import (CategorySerializer, ProductSerializer,
                                 ProviderSerializer)


def home(request):
    return render(request, 'product/pages/home.html')


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
