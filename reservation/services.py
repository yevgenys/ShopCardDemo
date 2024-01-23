import random

from card.models import CardItem


class ReservationService:
    def reserve_async(self, card_item: CardItem, sub_quantity: int) -> int:
        return random.randint(1, 10000)

    def check(self, id_: int):
        pass
