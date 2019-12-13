from django.contrib import admin
from .models import Product, Order

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    ''' product  '''
    list_display = ['id', 'product_name', 'description', 'price', 'image', 'user']

class OrderAdmin(admin.ModelAdmin):
    ''' order '''
    list_display = ['id', 'product', 'user', 'buying_date', 'price']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
