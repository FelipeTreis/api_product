from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('provider', views.providers, name='products'),
    path('category', views.categorys, name='cstegory'),
    path('product', views.products, name='product'),
]
