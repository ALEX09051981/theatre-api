from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from theatre.models import Genre


class GenreAPITests(APITestCase):
    def test_create_genre(self):
        url = reverse('theatre:genre-list')
        data = {"name": "Tragedy"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Genre.objects.count(), 1)

    def test_list_genres(self):
        Genre.objects.create(name="Comedy")
        url = reverse('theatre:genre-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
