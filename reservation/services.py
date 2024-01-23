import random

from django.db import transaction

from card.models import CardItem
from reservation.models import Reservation


class ReservationService:
    def reserve_async(self, card_item: CardItem, sub_quantity: int) -> int:
        reservation = Reservation()
        reservation.quantity = sub_quantity
        reservation.card_item = card_item

        card_item.quantity -= sub_quantity

        with transaction.atomic():
            reservation.save()
            card_item.save()

            return reservation.id

    def check(self, reservation_id: int):
        pass
