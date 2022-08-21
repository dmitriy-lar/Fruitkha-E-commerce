from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewsLetterForm
from .models import Category, Product


def page_not_found_view(request, exception):
    return render(request, 'store/404.html', status=404)


def newsletter_handler(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully subscribed!')
            return redirect('home_page')
    else:
        form = NewsLetterForm()
    return form


def home_page(request):
    products = Product.objects.all()[:3]
    context = {
        'products': products,
        'form': newsletter_handler(request)
    }
    return render(request, 'store/index.html', context)


def shop_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    paginator = Paginator(products, 6)
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
        'page_request_value': page_request_value,
        'form': newsletter_handler(request),
    }

    return render(request, 'store/shop.html', context)


def cart_page(request):
    context = {
        'form': newsletter_handler(request),
    }
    return render(request, 'store/cart.html', context)


def single_product_page(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:3]
    context = {
        'product': product,
        'related_products': related_products,
        'form': newsletter_handler(request),
    }
    return render(request, 'store/single-product.html', context)


def category_page(request, category_slug):
    categories = Category.objects.all()
    current_category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category__slug=category_slug)

    paginator = Paginator(products, 6)
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
        'page_request_value': page_request_value,
        'form': newsletter_handler(request),
        'current_category': current_category
    }
    return render(request, 'store/category.html', context)


def search(request):
    categories = Category.objects.all()

    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        products = products.filter(title__icontains=query)

    context = {
        'categories': categories,
        'products': products,
        'search_name': query,
    }
    return render(request, 'store/search.html', context)


