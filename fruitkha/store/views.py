from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .forms import NewsLetterForm
from .models import Category, Product


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
    products = Product.objects.all()

    paginator = Paginator(products, 1)
    page_request_value = 'page'
    page = request.GET.get(page_request_value)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'products': paginated_queryset,
        'page_request_value': page_request_value
    }

    return render(request, 'store/shop.html', context)


def cart_page(reqeust):
    return render(reqeust, 'store/cart.html')


def single_product_page(request):
    return render(request, 'store/single-product.html')
