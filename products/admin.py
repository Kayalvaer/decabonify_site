from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'image',
        'description',
        'price',
        
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
