from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

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
    path(
        'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path(
        'api/token/verify/', TokenVerifyView.as_view(), name='token_verify'
    ),
    path('', include(product_api_router.urls)),
]
