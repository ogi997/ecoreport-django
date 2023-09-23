from django.urls import path
from .views import UserCreateView, UserIdentityAPIView, UserChangeDataAPIView, ChangeUserPasswordAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("register/", UserCreateView.as_view(), name="user_registration"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("status/", UserIdentityAPIView.as_view(), name="user_status"),
    path("change-user-data/", UserChangeDataAPIView.as_view(), name="user_change_data"),
    path("change-user-password/", ChangeUserPasswordAPIView.as_view(), name="user_change_password"),
]
