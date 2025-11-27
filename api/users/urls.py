from django.urls import path
from .views import UserRetrieveUpdateAPIView,UserRegisterCreateAPIView,LoginAPIView,LogoutAPIView
urlpatterns = [
    path("user-info/",UserRetrieveUpdateAPIView.as_view(), name="user-info"),
    path("register/", UserRegisterCreateAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout")
]
