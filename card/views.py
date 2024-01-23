from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from card.models import CardItem
from card.serializers import CardItemSerializer, ReserveCardItemSerializer
from reservation.models import Reservation
from reservation.services import ReservationService


class CardItemsView(generics.ListCreateAPIView):
    permission_classes = []
    authentication_classes = []

    queryset = CardItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ReserveCardItemSerializer
        return CardItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item_from_db = self._validate_and_get_shop_item_from_db(serializer.validated_data)
        task_id = self._future_external_call(serializer.validated_data, item_from_db)
        return Response({"task_id": task_id}, status=status.HTTP_201_CREATED)

    def _validate_and_get_shop_item_from_db(self, validated_data: dict):
        object_from_db = get_object_or_404(
            CardItem.objects.filter(id=validated_data.get("id", -1))
        )
        if (object_from_db.quantity - validated_data.get("quantity", 0)) < 0:
            raise ValidationError("You trying to remove too many items. Reduce quantity and try again.")

        return object_from_db

    def _future_external_call(self, validated_data: dict, item_from_db: CardItem) -> int:
        reservation_service = ReservationService()
        return reservation_service.reserve_async(item_from_db, validated_data.get("quantity", 0))
