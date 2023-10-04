from django.urls import path

from .views import (ReportProblemListAPIView, ReportProblemUpdateDeleteAPIView, ExportToCSV,
                    GetAllReportProblemListAPIView)

urlpatterns = [
    # POST for create and GET for getting all problems
    path("create-problem/", ReportProblemListAPIView.as_view(), name="create_get_all_report_problem"),
    path("get-all/", GetAllReportProblemListAPIView.as_view(), name="get_all_data"),
    path("eco-problem/<int:pk>", ReportProblemUpdateDeleteAPIView.as_view(), name="retrieve_update_delete_problem"),
    path("get-csv/", ExportToCSV.as_view(), name="exporting_data_to_csv"),
]
