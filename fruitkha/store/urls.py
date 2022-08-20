from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('shop/', views.shop_page, name='shop_page'),
    path('cart/', views.cart_page, name='cart_page'),
    path('product/<slug:product_slug>/', views.single_product_page, name='single_product_page'),
    path('category/<slug:category_slug>/', views.category_page, name='category'),
    path('search/', views.search, name='search'),
]

