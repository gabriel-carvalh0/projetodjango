from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):

    lsit_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class ProductAdmin(admin.ModelAdmin):
    lsit_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created']


admin.site.register(Product, ProductAdmin),
admin.site.register(Category, CategoryAdmin)
