from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from theatre.models import (
    Play,
    TheatreHall,
    Genre,
    Actor
)
from django.utils import timezone


class PerformanceAPITests(APITestCase):
    def setUp(self):
        genre = Genre.objects.create(name="Drama")
        actor = Actor.objects.create(first_name="Kate", last_name="Winslet")
        self.play = Play.objects.create(title="Romeo", description="Love story")
        self.play.genres.add(genre)
        self.play.actors.add(actor)
        self.hall = TheatreHall.objects.create(name="Stage 1", rows=10, seats_in_row=10)

    def test_create_performance(self):
        url = reverse("theatre:performance-list")
        data = {
            "play_id": self.play.id,
            "theatre_hall_id": self.hall.id,
            "show_time":
                (timezone.now() + timezone.timedelta(days=1)).isoformat(),
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
