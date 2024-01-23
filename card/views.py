from rest_framework import generics

from card.models import CardItem
from card.serializers import CardItemSerializer


class CardItemsView(generics.ListCreateAPIView):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer
