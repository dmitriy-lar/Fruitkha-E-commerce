from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_page, name='cart_page'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>/', views.remove_item_from_cart, name='remove_from_cart'),
    path('update-cart-item-quantity/', views.update_cart_item_quantity, name='update_cart_item_quantity'),
]
