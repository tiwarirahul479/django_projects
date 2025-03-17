from django.contrib import admin

# Register your models here.
from .models import *

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['receipe_name', 'receipe_description', 'receipe_image', 'user']

admin.site.register(Receipe, RecipeAdmin)