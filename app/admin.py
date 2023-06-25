from django.contrib import admin
from .models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display="nombre","descripcion","precio","imagen"

admin.site.register(Producto,ProductoAdmin)