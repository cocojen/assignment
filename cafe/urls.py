from django.contrib import admin
from django.urls import include, path
from cafe.views import ProductsView

urlpatterns = [
    path("cafe/products", ProductsView.as_view(), name='products'),
    # path("cafe/product", ProductView.as_view(), name='product'),
]
