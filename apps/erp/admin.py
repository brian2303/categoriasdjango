from django.contrib import admin
from .models import Category,Product,Client,Sale,DetSale
# Register your models here.


"""
import model Category to admin
"""
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Sale)
admin.site.register(DetSale)