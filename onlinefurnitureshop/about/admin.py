from django.contrib import admin
from .models import Cart,Supplier,Colour,Size,Product,Order,Image


admin.site.register(Cart)
admin.site.register(Colour)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Size)
admin.site.register(Image)
