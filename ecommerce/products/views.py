from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def ecommerce_home(request):
    context = {
        'page': "Home"
    }
    return render(request, "base/base.html", context=context)

def shop_page(request):
    products_queryset = Product.objects.all()

    search_products = ''

    if request.GET.get("search_products"):
        search_products = request.GET.get("search_products")
        products_queryset = products_queryset.filter(product_name__icontains = search_products)

    paginator = Paginator(products_queryset, 16)
    page_number = request.GET.get("page")
    products_page_obj = paginator.get_page(page_number)

    context = {
        'products': products_page_obj,
        'page': "Shop",
        'search_products': search_products,
    }
    return render(request, "product/shop_page.html", context=context)

def product_page(request, uid):
    product_queryset = Product.objects.get(uid=uid)

    context = {
        'page': "Product",
        'product': product_queryset,
    }
    return render(request, "product/product_page.html", context=context)