from django.shortcuts import render, get_object_or_404
from store.models import Product
from cart.models import Cart
from cart.views import _get_session_id
from category.models import Category


def store(request, category_slug=None):
    if category_slug:
        cat = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=cat, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)

    try:
        cart = Cart.objects.get(session_id=_get_session_id(request))
    except:
        cart = None

    payload = {
        'cart': cart,
        'products': products,
    }

    return render(request, 'store.html', payload)


def product_detail(request, category_slug=None, product_slug=None):
    single_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    try:
        cart = Cart.objects.get(session_id=_get_session_id(request))
    except:
        cart = None

    payload = {
        'cart': cart,
        'product': single_product,
    }

    return render(request, 'product-detail.html', payload)

