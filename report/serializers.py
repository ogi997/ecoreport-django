from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import ReportProblem


class ReportProblemSerializers(GeoFeatureModelSerializer):
    class Meta:
        model = ReportProblem
        geo_field = "geometry"
        fields = (
            "id", "problem_type", "city", "title", "note", "image", "last_user", "active", "creation_date", "geometry"
        )


class GetAllReportProblemSerializers(GeoFeatureModelSerializer):
    class Meta:
        model = ReportProblem
        geo_field = "geometry"
        fields = (
            "id", "title", "note", "active"
        )
