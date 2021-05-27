from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop - Каталог', 'categories': ProductCategory.objects.all()}

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    if len(products)>0:
        paginator = Paginator(products, per_page=3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        context.update({'products': products_paginator})
    else:
        context.update({'message': 'В данной категории товаров нет!'})

    return render(request, 'mainapp/products.html', context)


def test_context(request):
    context = {
        'title': 'Test Context',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Михаил Герасимов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590.00},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890.00},
        ]
    }
    return render(request, 'mainapp/test_context.html', context)
