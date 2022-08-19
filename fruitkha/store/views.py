from django.shortcuts import render


def home_page(request):
    return render(request, 'store/index.html')


def shop_page(request):
    categories = ['All', 'Strawberry', 'Berry', 'Lemon']
    context = {
        'categories': categories
    }
    return render(request, 'store/shop.html', context)


def cart_page(reqeust):
    return render(reqeust, 'store/cart.html')
