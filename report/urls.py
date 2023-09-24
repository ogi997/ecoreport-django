from .views import ReportProblemListAPIView, ReportProblemUpdateDeleteAPIView, ExportToCSV
from django.urls import path

urlpatterns = [
    # POST for create and GET for getting all problems
    path("create-problem/", ReportProblemListAPIView.as_view(), name="create_get_all_report_problem"),
    path("eco-problem/<int:pk>", ReportProblemUpdateDeleteAPIView.as_view(), name="retrieve_update_delete_problem"),
    path("get-csv/", ExportToCSV.as_view(), name="exporting_data_to_csv"),
]