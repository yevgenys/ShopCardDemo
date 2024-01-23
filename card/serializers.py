from django.core import validators
from rest_framework import serializers

from card.models import CardItem


class ReserveCardItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        required=True,
        validators=[
            validators.MinValueValidator(1)
        ]
    )

    quantity = serializers.IntegerField(
        required=True,
        validators=[
            validators.MinValueValidator(1)
        ]
    )

    class Meta:
        fields = ("id", "quantity")


class CardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = '__all__'
