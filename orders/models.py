from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product


User = get_user_model()

STATUS_CHOICE = (
    ('open', 'Открытый'),
    ('in_process', 'В обработке'),
    ('canceled', 'Отмененный'),
    ('finished', 'Завершенный')
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='orders')
    create_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=150, blank=True)
    productcs = models.ManyToManyField(Product, through='OrderItems')
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='open')

    def __str__(self) -> str:
        return f'Order #{self.id}'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveSmallIntegerField(default=0)