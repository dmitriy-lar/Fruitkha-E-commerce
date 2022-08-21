from django.shortcuts import render

from store.views import newsletter_handler


def cart_page(request):
    context = {
        'form': newsletter_handler(request),
    }
    return render(request, 'cart/cart.html', context)