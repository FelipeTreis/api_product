from django.shortcuts import render


def home(request):
    return render(request, 'product/pages/home.html')
