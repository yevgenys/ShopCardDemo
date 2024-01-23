from rest_framework import serializers

from card.models import CardItem


class CardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = '__all__'
