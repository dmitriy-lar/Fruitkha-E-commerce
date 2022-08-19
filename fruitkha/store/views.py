from django.shortcuts import render


def home_page(request):
    return render(request, 'store/index.html')


def shop_page(request):
    return render(request, 'store/shop.html')
