from django.contrib import admin
from .models import Colour,Size,Product,Cart,Supplier,Order

admin.site.register(Colour)
admin.site.register(Order)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Supplier)

# Register your models here.
