from django.contrib import admin
from .models import (
    Genre,
    Actor,
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket,
)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    filter_horizontal = ('genres', 'actors')


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rows', 'seats_in_row', 'capacity')
    search_fields = ('name',)


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'play', 'theatre_hall', 'show_time')
    list_filter = ('play', 'theatre_hall', 'show_time')
    search_fields = ('play__title',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'performance', 'created_at')
    list_filter = ('performance', 'user', 'created_at')
    search_fields = ('user__username',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'reservation', 'row', 'seat')
    list_filter = ('reservation', 'row')
    search_fields = ('reservation__user__username',)
