from rest_framework import serializers

from report.models import ReportProblem
from users.models import User


class ActivateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportProblem
        fields = ["id", "active"]

    def update(self, instance, validated_data):
        instance.active = True
        instance.save()
        return instance


class DeactivateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportProblem
        fields = ["id", "active"]

    def update(self, instance, validated_data):
        instance.active = False
        instance.save()

        return instance


class ActivateUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "is_active"]

    def update(self, instance, validated_data):
        instance.is_active = True
        instance.save()

        return instance


class DeactivateUserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "is_active"]

    def update(self, instance, validated_data):
        instance.is_active = False
        instance.save()

        return instance


class MakeUserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "is_admin"]

    def update(self, instance, validated_data):
        instance.is_admin = True
        instance.save()

        return instance


class RemoveAdminFromUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "is_admin"]

    def update(self, instance, validated_data):
        instance.is_admin = False
        instance.save()

        return instance


class GetAllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "is_active", "is_admin"]


class GetAllReportProblem(serializers.ModelSerializer):
    class Meta:
        model = ReportProblem
        fields = ["id", "title", "active"]
