from django.db import models
from store.models import Product


class CartItem(models.Model):
    session_id = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} : {self.quantity}"

    def get_total_price(self):
        return round(self.quantity * self.product.price, 2)


class Cart(models.Model):
    session_id = models.CharField(max_length=255)
    item = models.ManyToManyField(CartItem)

    def __str__(self):
        return self.session_id

    def get_total_price(self):
        items = CartItem.objects.filter(session_id=self.session_id)
        total_price = float(0)
        for item in items:
            total_price += item.get_total_price()

        return total_price

    def get_total_quantity(self):
        return len(self.item.all())





