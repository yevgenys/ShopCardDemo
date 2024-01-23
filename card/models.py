from django.db import models


class CardItem(models.Model):
    name = models.CharField(max_length=256)
    quantity = models.IntegerField()
