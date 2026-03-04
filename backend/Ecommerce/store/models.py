from django.db import models
from auth.models import Userprofile
import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2050, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=500, default='', blank=True, null=True)
    phone = models.CharField(max_length=20, default='', blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product.name + ' ' + self.user.name