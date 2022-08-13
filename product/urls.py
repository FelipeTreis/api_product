from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('', views.home, name='home'),
    path('provider', views.providers, name='provider'),
    path('category', views.categorys, name='category'),
    path('product', views.products, name='product'),
]
