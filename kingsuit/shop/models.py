from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(default='https://via.placeholder.com/150')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name