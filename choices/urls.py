from django.urls import path
from .views import CityListAPIView, EventTypeListAPIView

urlpatterns = [
    path("cities/", CityListAPIView.as_view(), name="cities"),
    path("event-type/", EventTypeListAPIView.as_view(), name="event-types"),
]