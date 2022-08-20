from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import NewsLetterForm
from .models import Category

def home_page(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully subscribed!')
            return redirect('home_page')
    else:
        form = NewsLetterForm()

    context = {
        'form': form
    }
    return render(request, 'store/index.html', context)


def shop_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'store/shop.html', context)


def cart_page(reqeust):
    return render(reqeust, 'store/cart.html')


def single_product_page(request):
    return render(request, 'store/single-product.html')
