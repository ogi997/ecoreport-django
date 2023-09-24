import csv

from django.shortcuts import render
from rest_framework import generics
from .models import ReportProblem
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import ReportProblemSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework_gis.filters import InBBoxFilter
from rest_framework.views import APIView
from django.http import HttpResponse


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


class ExportToCSV(APIView):

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        writer = csv.writer(response)
        # formatOfCsvFile = ["naslov", "opis", "link", "datum_objavljivanja"]
        # writer = csv.DictWriter(file, fieldnames=formatOfCsvFile)
        # writer.writeheader()
        for data in ReportProblem.objects.all():
            # print(data.geometry.)
            row = {
                data.title,
                data.note,
                data.geometry[0],
                data.geometry[1],
            }
            
            writer.writerow(row)

        return response
