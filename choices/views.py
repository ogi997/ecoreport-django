from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import City, EventType
from .serializer import ModelSerializer
from rest_framework.permissions import AllowAny


class ModelListAPIView(ListAPIView):
    serializer_class = (ModelSerializer)
    permission_classes = (AllowAny,)


class CityListAPIView(ModelListAPIView):
    queryset = [{"code": item[0], "name": item[1]} for item in City.choices]


class EventTypeListAPIView(ModelListAPIView):
    queryset = [{"code": item[0], "name": item[1]} for item in EventType.choices]
