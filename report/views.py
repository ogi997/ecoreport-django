from django.shortcuts import render
from rest_framework import generics
from .models import ReportProblem
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import ReportProblemSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework_gis.filters import InBBoxFilter
# Create your views here.


class ReportProblemListAPIView(generics.ListCreateAPIView):
    queryset = ReportProblem.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReportProblemSerializers
    filter_backends = [SearchFilter, DjangoFilterBackend, InBBoxFilter]
    bbox_filter_field = "geometry"
    # filterset_fields = ['entity', 'canton', 'zone']
    search_fields = ['city']

    def perform_create(self, serializer):
        serializer.save(last_user=self.request.user)


class ReportProblemUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportProblem.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReportProblemSerializers

    def perform_create(self, serializer):
        serializer.save(last_user=self.request.user)
