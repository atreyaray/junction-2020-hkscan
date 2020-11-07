from django.db import models
from django.utils import timezone

class Product(models.Model):
    productType = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    description = models.TextField()
    Recipe = models.TextField()
    RecipeLink = models.TextField()
    media = models.TextField()
    Price = models.DecimalField(decimal_places=2, max_digits=100)
    recipe_name = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    recipe_main = models.TextField()

    def __str__(self):
        return f"{self.productType}: {self.product_name}" 