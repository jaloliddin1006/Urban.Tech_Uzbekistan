from django.contrib import admin
from .models import Users,Stores,Products
# Register your models here.
admin.site.register(Users)
admin.site.register(Stores)
admin.site.register(Products)