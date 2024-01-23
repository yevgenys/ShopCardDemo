from rest_framework import generics

from card.models import CardItem
from card.serializers import CardItemSerializer, ReserveCardItemSerializer


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
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

