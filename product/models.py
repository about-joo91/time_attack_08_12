from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class UserProduct(models.Model):
    buy_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    product = models.ForeignKey('Product', null=True , on_delete=models.SET_NULL)