from django.contrib.auth.models import User
from django.db import models

from store.models import Product


class OrderItem(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} - {self.product.title}"

    def get_single_total_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.client.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_single_total_price()
        return total