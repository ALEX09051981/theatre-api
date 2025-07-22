from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from theatre.models import TheatreHall

class TheatreHallAPITests(APITestCase):
    def test_create_theatre_hall(self):
        url = reverse("theatre:theatrehall-list")
        data = {"name": "Main Hall", "rows": 10, "seats_in_row": 20}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_theatre_halls(self):
        TheatreHall.objects.create(name="Big Hall", rows=12, seats_in_row=30)
        url = reverse("theatre:theatrehall-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        