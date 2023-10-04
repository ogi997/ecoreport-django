from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import City, EventType
from .serializer import ModelSerializer


class ModelListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ModelSerializer


class CityListAPIView(ModelListAPIView):
    permission_classes = (AllowAny,)
    queryset = [{"code": item[0], "name": item[1]} for item in City.choices]


class EventTypeListAPIView(ModelListAPIView):
    permission_classes = (AllowAny,)
    queryset = [{"code": item[0], "name": item[1]} for item in EventType.choices]
