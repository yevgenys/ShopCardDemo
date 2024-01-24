from unittest.mock import patch

from django.test import TestCase

from card.models import CardItem
from reservation.models import Reservation
from reservation.services import ReservationService


class TestThirdPartyApiIsCalled(TestCase):
    TEST_VALUE = 100

    def setUp(self):
        self._system_under_test = ReservationService()
        # add test data
        self._test_item = CardItem(
            name="test", quantity=self.TEST_VALUE
        )
        self._test_item.save()

    def test_db_objects_are_saved(self):
        """
        Tests that after triggering reserve_async method:
         1. new record Reservation is saved.
         2. CardItem is assigned to the new Reservation.
         3. both objects are saved to DB
         4. CardItem quantity was modified
        """

        subtract_arg = 10

        self.assertEqual(Reservation.objects.count(), 0)

        self._system_under_test.reserve_async(self._test_item, subtract_arg)

        fresh_db_object = CardItem.objects.get(pk=self._test_item.pk)
        expected_value = self.TEST_VALUE - subtract_arg
        self.assertEqual(fresh_db_object.quantity, expected_value)
        self.assertEqual(Reservation.objects.count(), 1)

        reservation = Reservation.objects.last()
        self.assertEqual(reservation.card_item, self._test_item)

    @patch('reservation.services.call_reserve_external.delay')
    def test_external_call_after_transaction_commit(self, mock_task):
        subtract_arg = 12

        self.assertEqual(Reservation.objects.count(), 0)

        with self.captureOnCommitCallbacks(execute=True):
            self._system_under_test.reserve_async(self._test_item, subtract_arg)

        self.assertEqual(Reservation.objects.count(), 1)
        mock_task.assert_called_once_with(1)
