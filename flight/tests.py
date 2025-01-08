
from django.test import TestCase
from .models import Flight
from .serializers import FlightSerializer

# flight_number unique testi;
class FlightSerializerTest(TestCase):
    def test_flight_serializer(self):
        data = {
            "flight_number": "AB123",
            "operation_airlines": "Test Airlines",
            "departure_city": "Istanbul",
            "arrival_city": "Ankara",
            "date_of_departure": "2025-01-10",
            "estimated_time_of_departure": "12:00:00"
        }
        serializer = FlightSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(Flight.objects.count(), 1)
