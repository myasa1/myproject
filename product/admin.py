from django.contrib import admin

# Register your models here.
from .models import product
from .models import ProductImage



admin.site.register(product)
admin.site.register(ProductImage)