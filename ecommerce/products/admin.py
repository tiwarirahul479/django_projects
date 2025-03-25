from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'category', 'product_description']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_image']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
