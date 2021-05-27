from django.contrib import admin
from mainapp.models import ProductCategory, Product
from authapp.models import User

# Register your models here.
admin.site.register(ProductCategory)
# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('image', 'name', 'description', ('price', 'quantity'))
    readonly_fields = ('description', )
    ordering = ('-price',)  # сортировка от я до а: добавляется знак "-"#
    search_fields = ('name',)



