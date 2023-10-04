from django.urls import path

from .views import (ActivateReportAPIView, DeactivateReportAPIView,
                    ActivateUserAccountAPIView, DeactivateUserAccountAPIView,
                    MakeUserAdminAPIView, RemoveAdminFromUserAPIView,
                    GetAllUsersAPIView, GetAllReportProblemAPIView)

urlpatterns = [
    # POST for create and GET for getting all problems
    path("activate-report/<int:pk>", ActivateReportAPIView.as_view(), name="activate_report"),
    path("deactivate-report/<int:pk>", DeactivateReportAPIView.as_view(), name="deactivate_report"),

    path("activate-user/<int:pk>", ActivateUserAccountAPIView.as_view(), name="activate_user_account"),
    path("deactivate-user/<int:pk>", DeactivateUserAccountAPIView.as_view(), name="deactivate_user_account"),
    path("make-user-admin/<int:pk>", MakeUserAdminAPIView.as_view(), name="make_user_admin"),
    path("remove-admin-user/<int:pk>", RemoveAdminFromUserAPIView.as_view(), name="remove_admin_from_user"),

    path("get-all-users/", GetAllUsersAPIView.as_view(), name="get_all_users"),
    path("get-all-report-problem/", GetAllReportProblemAPIView.as_view(), name="get_all_report_problem_api_view"),
]
