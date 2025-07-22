from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreViewSet,
    ActorViewSet,
    PlayViewSet,
    TheatreHallViewSet,
    PerformanceViewSet,
    ReservationViewSet,
    TicketViewSet,
)

router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'actors', ActorViewSet, basename='actor')
router.register(r'plays', PlayViewSet, basename='play')
router.register(r'theatre-halls', TheatreHallViewSet, basename='theatrehall')
router.register(r'performances', PerformanceViewSet, basename='performance')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'tickets', TicketViewSet, basename='ticket')

urlpatterns = [
    path('', include(router.urls)),
]
