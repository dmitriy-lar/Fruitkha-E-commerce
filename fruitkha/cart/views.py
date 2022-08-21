from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from store.views import newsletter_handler
from .models import Product, OrderItem, Order


@login_required
def cart_page(request):
    try:
        order = Order.objects.get(client=request.user, ordered=False)
    except ObjectDoesNotExist:
        order = []

    context = {
        'order': order,
        'form': newsletter_handler(request),
    }
    return render(request, 'cart/cart.html', context)


@login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        client=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(client=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__slug=product.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
            return redirect('shop_page')
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to you cart")
            return redirect('shop_page')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            client=request.user, ordered_date=ordered_date
        )
        order.items.add(order_item)
        messages.info(request, "This item was added to you cart")
        return redirect('shop_page')


@login_required
def remove_item_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        client=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__slug=product.slug).exists():
            order_item = OrderItem.objects.filter(
                product=product,
                client=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart")
            return redirect('cart_page')
        else:
            messages.info(request, "This item was not in you cart")
            return redirect('cart_page')
    else:
        messages.info(request, "You do not have an active order")
        return redirect('cart_page')


@login_required
def update_cart_item_quantity(request):
    order = Order.objects.get(client=request.user, ordered=False)
    titles = []
    cnt = 0
    for order_item in order.items.all():
        titles.append(order_item.product.title)
        item_quantity = request.POST[titles[cnt]]
        order_item.quantity = item_quantity
        order_item.save()
        if int(item_quantity) <= 0:
            order.items.remove(order_item)
            order_item.delete()
        cnt += 1
    messages.info(request, "Your cart was updated")
    return redirect('cart_page')
