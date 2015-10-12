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
    bedrooms = models.IntegerField()
    kitchens = models.IntegerField()
    bathrooms = models.IntegerField()

    def __str__(self):
        return self.title
