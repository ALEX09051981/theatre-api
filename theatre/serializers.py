from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket
)

User = get_user_model()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class PlaySerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    genre_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        write_only=True,
        source="genres"
    )

    actors = ActorSerializer(many=True, read_only=True)
    actor_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all(), write_only=True, source="actors"
    )

    class Meta:
        model = Play
        fields = (
            "id",
            "title",
            "description",
            "genres",
            "genre_ids",
            "actors",
            "actor_ids",
        )


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")
        read_only_fields = ("capacity",)


class PerformanceSerializer(serializers.ModelSerializer):
    play = PlaySerializer(read_only=True)
    play_id = serializers.PrimaryKeyRelatedField(
        queryset=Play.objects.all(), source="play", write_only=True
    )

    theatre_hall = TheatreHallSerializer(read_only=True)
    theatre_hall_id = serializers.PrimaryKeyRelatedField(
        queryset=TheatreHall.objects.all(),
        source="theatre_hall",
        write_only=True
    )

    class Meta:
        model = Performance
        fields = (
            "id",
            "play",
            "play_id",
            "theatre_hall",
            "theatre_hall_id",
            "show_time",
        )


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "reservation")


class ReservationSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)
    performance_id = serializers.PrimaryKeyRelatedField(
        queryset=Performance.objects.all(),
        source="performance",
        write_only=True
    )

    class Meta:
        model = Reservation
        fields = ("id", "user", "performance_id", "created_at", "tickets")
        read_only_fields = ("user", "created_at")


class PlayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id", "image")
