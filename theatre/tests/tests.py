from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from theatre.models import (
    Genre, Actor, Play, Performance,
    Reservation, TheatreHall, Ticket
)
from django.utils import timezone

User = get_user_model()


class GenreTests(APITestCase):
    def test_create_genre(self):
        url = reverse('theatre:genre-list')
        data = {'name': 'Comedy'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Genre.objects.count(), 1)
        self.assertEqual(Genre.objects.get().name, 'Comedy')

    def test_list_genres(self):
        Genre.objects.create(name='Drama')
        url = reverse('theatre:genre-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class ActorTests(APITestCase):
    def test_create_actor(self):
        url = reverse('theatre:actor-list')
        data = {'first_name': 'John', 'last_name': 'Doe'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.count(), 1)
        self.assertEqual(Actor.objects.get().first_name, 'John')


class PlayTests(APITestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name='Tragedy')
        self.actor = Actor.objects.create(first_name='Jane', last_name='Smith')

    def test_create_play(self):
        genre = Genre.objects.create(name="Drama")
        actor = Actor.objects.create(first_name="Tom", last_name="Hanks")

        data = {
            "title": "Hamlet",
            "description": "A classic play",
            "genre_ids": [genre.id],
            "actor_ids": [actor.id],
        }

        url = reverse("theatre:play-list")
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Play.objects.count(), 1)

        play = Play.objects.get()

        self.assertEqual(play.title, 'Hamlet')
        self.assertEqual(play.genres.first(), genre)
        self.assertEqual(play.actors.first(), actor)


class ReservationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='pass1234'
        )
        self.client.force_authenticate(user=self.user)

        genre = Genre.objects.create(name='Drama')
        actor = Actor.objects.create(first_name='Tom', last_name='Hanks')
        play = Play.objects.create(title='Hamlet', description='A classic play')
        play.genres.add(genre)
        play.actors.add(actor)

        theatre_hall = TheatreHall.objects.create(
            name='Main Hall', rows=10, seats_in_row=20
        )

        self.performance = Performance.objects.create(
            play=play,
            theatre_hall=theatre_hall,
            show_time=timezone.now() + timezone.timedelta(days=1)
        )


class PerformanceTests(TestCase):
    def setUp(self):
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=20
        )
        self.play = Play.objects.create(title="Hamlet", description="Classic play")

    def test_create_performance(self):
        show_time = timezone.now() + timezone.timedelta(days=1)
        performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=show_time
        )
        self.assertEqual(performance.play, self.play)
        self.assertEqual(performance.theatre_hall, self.theatre_hall)
        self.assertEqual(performance.show_time, show_time)
        self.assertEqual(str(performance),
                         f"{self.play.title} at {show_time}")


class TicketModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="12345678",
            first_name="Test",
            last_name="User"
        )
        self.play = Play.objects.create(title="Hamlet", description="Classic")
        self.theatre_hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=20
        )
        self.performance = Performance.objects.create(
            play=self.play,
            theatre_hall=self.theatre_hall,
            show_time=timezone.now() + timezone.timedelta(days=1)
        )
        self.reservation = Reservation.objects.create(
            user=self.user, performance=self.performance
        )

    def test_create_ticket(self):
        ticket = Ticket.objects.create(
            reservation=self.reservation, row=1, seat=5
        )
        self.assertEqual(ticket.row, 1)
        self.assertEqual(ticket.seat, 5)
        self.assertEqual(
            str(ticket),
            f"Ticket: row 1, seat 5 for reservation {self.reservation.id}"
        )

    def test_unique_together_constraint(self):
        Ticket.objects.create(reservation=self.reservation, row=1, seat=5)
        with self.assertRaises(Exception):
            Ticket.objects.create(reservation=self.reservation, row=1, seat=5)


class TheatreHallModelTests(TestCase):
    def test_create_theatre_hall(self):
        hall = TheatreHall.objects.create(
            name="Main Hall", rows=10, seats_in_row=20
        )
        self.assertEqual(hall.name, "Main Hall")
        self.assertEqual(hall.rows, 10)
        self.assertEqual(hall.seats_in_row, 20)

    def test_capacity_property(self):
        hall = TheatreHall.objects.create(
            name="Main Hall", rows=5, seats_in_row=15
        )
        expected_capacity = 5 * 15
        self.assertEqual(hall.capacity, expected_capacity)
