from django.urls import path

from reservation.views import ReservationItemView

urlpatterns = [
    path('<pk>', ReservationItemView.as_view(), name='reservations'),
]
