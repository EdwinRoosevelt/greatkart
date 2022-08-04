"""greatkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from greatkart.views import home
from store import views
from cart.views import cart, add_to_cart, remove_from_cart, decrement_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('store/', views.store, name='store'),
    path('store/<slug:category_slug>/', views.store, name='product_by_category'),
    path('store/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('cart/add_product/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove_product/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/remove_one_product/<int:product_id>/', decrement_from_cart, name='decrement_from_cart')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
