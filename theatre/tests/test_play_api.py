from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from theatre.models import Play, Genre, Actor


class PlayAPITests(APITestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name="Drama")
        self.actor = Actor.objects.create(first_name="Jane", last_name="Doe")

    def test_create_play(self):
        url = reverse("theatre:play-list")
        data = {
            "title": "Hamlet",
            "description": "Classic tragedy",
            "genre_ids": [self.genre.id],
            "actor_ids": [self.actor.id],
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Play.objects.count(), 1)
