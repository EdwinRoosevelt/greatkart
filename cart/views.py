from django.shortcuts import render, redirect
from store.models import Product
from cart.models import CartItem, Cart


def _get_session_id(request):
    session_id = request.session.session_key
    if not session_id:
        session_id = request.session.create()
    return session_id


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    session_id = _get_session_id(request)

    # check if the cart item exists or create one
    try:
        item = CartItem.objects.get(session_id=session_id, product=product)
        item.quantity += 1
        item.save()

    except CartItem.DoesNotExist:
        item = CartItem.objects.create(
            session_id=session_id,
            product=product,
            quantity=1
        )

    # check if the cart exists or create a new one.
    try:
        cart = Cart.objects.get(session_id=session_id)

    except Cart.DoesNotExist:

        cart = Cart.objects.create(
            session_id=session_id,
        )

    # check if the cart item is related to the cart.
    existing_items = cart.item.all()
    if item not in existing_items:
        cart.item.add(item)

    return redirect('cart')


def remove_from_cart(request, product_id):
    session_id = _get_session_id(request)
    try:
        CartItem.objects.get(session_id=session_id, product__id=product_id).delete()

    except:
        pass

    return redirect('cart')


def decrement_from_cart(request, product_id):
    session_id = _get_session_id(request)
    try:
        item = CartItem.objects.get(session_id=session_id, product__id=product_id)
        item.quantity -= 1
        item.save()

    except:
        pass

    return redirect('cart')


def cart(request):
    try:
        cart = Cart.objects.get(session_id=_get_session_id(request))
    except:
        cart = None

    cart_items = CartItem.objects.filter(session_id=_get_session_id(request))

    payload = {
        'cart': cart,
        'cart_items': cart_items

    }
    return render(request, 'cart.html', payload)
