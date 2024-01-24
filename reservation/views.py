from django.db.models import Sum
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from card.models import CardItem
from card.serializers import CardItemSerializer, ReserveCardItemSerializer
from reservation.models import Reservation, PENDING
from reservation.serializers import ReservationItemSerializer
from reservation.services import ReservationService


class ReservationItemView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Reservation.objects.all()
    serializer_class = ReservationItemSerializer


