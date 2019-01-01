from django.contrib import admin
from .models import Type, Product

class TypeModelAdmin(admin.ModelAdmin):
    list_filter = ('active',)
    list_display = ('name', 'active', )

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'description')

admin.site.register(Type, TypeModelAdmin)
admin.site.register(Product, ProductModelAdmin)