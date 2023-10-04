import csv

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework_gis.filters import InBBoxFilter

from .models import ReportProblem
from .serializers import ReportProblemSerializers, GetAllReportProblemSerializers


# Create your views here.
class GetAllReportProblemListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = ReportProblem.objects.filter(active=True)
    serializer_class = GetAllReportProblemSerializers


class ReportProblemListAPIView(generics.ListCreateAPIView):
    queryset = ReportProblem.objects.filter(active=True)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReportProblemSerializers
    filter_backends = [SearchFilter, DjangoFilterBackend, InBBoxFilter]
    filterset_fields = ['problem_type']

    def perform_create(self, serializer):
        serializer.save(last_user=self.request.user)


class ReportProblemUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportProblem.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReportProblemSerializers

    def perform_create(self, serializer):
        serializer.save(last_user=self.request.user)


class ExportToCSV(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        writer = csv.writer(response)

        for data in ReportProblem.objects.all():
            row = {
                data.title,
                data.note,
                data.geometry[0],
                data.geometry[1],
            }

            writer.writerow(row)

        return response
