from django.urls import path

from card.views import CardItemsView

urlpatterns = [
    path('items/', CardItemsView.as_view(), name='items'),
]
