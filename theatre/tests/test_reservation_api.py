from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from theatre.models import Reservation, Performance, Play, TheatreHall, Genre, Actor
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class ReservationAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="12345678",
            first_name="Test",
            last_name="User"
        )
        self.client.force_authenticate(user=self.user)

        genre = Genre.objects.create(name="Comedy")
        actor = Actor.objects.create(first_name="Jim", last_name="Carrey")
        play = Play.objects.create(title="Mask", description="Fun play")
        play.genres.add(genre)
        play.actors.add(actor)

        hall = TheatreHall.objects.create(name="Comedy Hall", rows=5, seats_in_row=5)
        self.performance = Performance.objects.create(
            play=play,
            theatre_hall=hall,
            show_time=timezone.now() + timezone.timedelta(days=2)
        )

    def test_create_reservation(self):
        url = reverse("theatre:reservation-list")
        data = {
            "performance_id": self.performance.id,
            "tickets": [{"row": 1, "seat": 2}, {"row": 1, "seat": 3}]
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
