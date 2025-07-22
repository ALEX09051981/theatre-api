from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from theatre.models import Actor

class ActorAPITests(APITestCase):
    def test_create_actor(self):
        url = reverse('theatre:actor-list')
        data = {"first_name": "Tom", "last_name": "Hanks"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.count(), 1)

    def test_list_actors(self):
        Actor.objects.create(first_name="Emma", last_name="Stone")
        url = reverse('theatre:actor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        