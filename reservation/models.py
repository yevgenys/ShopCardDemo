from datetime import timedelta

from django.conf import settings
from django.core import validators
from django.db import models
from django.utils import timezone

from card.models import CardItem

PENDING = "PENDING"
FAILED = "FAILED"
FINISHED = "FINISHED"

RESERVATION_STATUS = [
    (PENDING, "Pending"),
    (FINISHED, "Finished"),
    (FAILED, "Failed"),
]


def calc_expiration_date():
    return timezone.now() + timedelta(minutes=settings.RESERVATION_EXPIRATION)


class Reservation(models.Model):
    reservation_id = models.CharField(max_length=32)
    status = models.CharField(max_length=32, choices=RESERVATION_STATUS, default=PENDING)
    quantity = models.IntegerField(validators=[
        validators.MinValueValidator(1)
    ])
    card_item = models.ForeignKey(CardItem, on_delete=models.CASCADE, related_name="reservations")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    expire = models.DateTimeField(default=calc_expiration_date)
