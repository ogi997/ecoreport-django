# from django.shortcuts import render
from rest_framework import generics

from report.models import ReportProblem
from users.models import User
from users.permissions import IsAdminUser
from .serializers import (ActivateReportSerializer, DeactivateReportSerializer,
                          ActivateUserAccountSerializer, DeactivateUserAccountSerializer,
                          MakeUserAdminSerializer, RemoveAdminFromUserSerializer,
                          GetAllUsersSerializer, GetAllReportProblem)


# Create your views here.
class ActivateReportAPIView(generics.UpdateAPIView):
    queryset = ReportProblem.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = ActivateReportSerializer


class DeactivateReportAPIView(generics.UpdateAPIView):
    queryset = ReportProblem.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = DeactivateReportSerializer


class ActivateUserAccountAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = ActivateUserAccountSerializer


class DeactivateUserAccountAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = DeactivateUserAccountSerializer


class MakeUserAdminAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = MakeUserAdminSerializer


class RemoveAdminFromUserAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = RemoveAdminFromUserSerializer


class GetAllUsersAPIView(generics.ListAPIView):
    queryset = User.objects.filter(is_superuser=False)
    permission_classes = (IsAdminUser,)
    serializer_class = GetAllUsersSerializer


class GetAllReportProblemAPIView(generics.ListAPIView):
    queryset = ReportProblem.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = GetAllReportProblem
