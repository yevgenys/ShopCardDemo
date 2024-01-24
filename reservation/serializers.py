from rest_framework import serializers

from reservation.models import Reservation


class ReservationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
