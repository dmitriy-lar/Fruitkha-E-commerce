from django import template
from cart.models import Order

register = template.Library()


@register.filter
def cart_item_count(client):
    if client.is_authenticated:
        qs = Order.objects.filter(client=client, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
