"""
property models
"""

from django.db import models


class House(models.Model):
    """
    creates table: house
    """
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    address = models.TextField()
    bedrooms = models.IntegerField(verbose_name='No of Bedrooms')
    kitchens = models.IntegerField(verbose_name='No of Bedrooms')
    bathrooms = models.IntegerField(verbose_name='No of Bedrooms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
