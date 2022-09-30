from django.contrib import admin
from .models import Products, Cart,Shirt,Runner

# Register your models here.
admin.site.register(Products)
admin.site.register(Shirt)
admin.site.register(Runner)
admin.site.register(Cart)


