from django.db import models

from card.models import CardItem

RESERVATION_STATUS = [
    ("PENDING", "Pending"),
    ("FINISHED", "Finished"),
]


class Reservation(models.Model):
    reservation_id = models.CharField(max_length=32)
    status = models.CharField(max_length=32, choices=RESERVATION_STATUS)
    card_item = models.ForeignKey(CardItem, on_delete=models.CASCADE, related_name="reservation")
