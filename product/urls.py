from django.urls import include, path
from rest_framework.routers import SimpleRouter

from product import views

app_name = 'product'

product_api_router = SimpleRouter()
product_api_router.register(
    'provider', views.ProviderApiViewSet, basename='provider')
product_api_router.register(
    'category', views.CategoryApiViewSet, basename='category')
product_api_router.register(
    'product', views.ProductApiViewSet, basename='product')

urlpatterns = [
    path('', include(product_api_router.urls)),
]
