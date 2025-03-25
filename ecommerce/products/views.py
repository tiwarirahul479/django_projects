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

    paginator = Paginator(products_queryset, 16)
    page_number = request.GET.get("page")
    products_page_obj = paginator.get_page(page_number)

    context = {
        'products': products_page_obj,
        'page': "Shop"
    }
    return render(request, "product/shop_page.html", context=context)