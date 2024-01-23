import requests
from celery import shared_task
from django.conf import settings
from django.db import transaction
from rest_framework import status

from reservation.models import Reservation, FINISHED, FAILED


@shared_task
def call_reserve_external(reservation_id: int):
    reservation = Reservation.objects.get(pk=reservation_id)

    host = settings.EXTERNAL_RESERVATION_API_CONN_STR
    response = requests.post(host, json={"id": reservation.card_item.id})
    if response.status_code != status.HTTP_201_CREATED:
        print(f"[Error]: wrong status code. status_code =  {response.status_code}, content: {response.content.decode('utf-8')}")

        _fail_reservation(reservation)

    data = response.json()
    if data.get("status", "failed") == "ok":
        reservation.reservation_id = data["reservation_id"]
        reservation.status = FINISHED
        reservation.save()
    else:
        print(f"[Error]: wrong data status. content: {data}")
        _fail_reservation(reservation)


def _fail_reservation(reservation):
    with transaction.atomic():
        # release lock items
        reservation.card_item.quantity += reservation.quantity

        reservation.status = FAILED
        reservation.save()
