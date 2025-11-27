from django.urls import path
from .views import UserRetrieveUpdateAPIView,UserRegisterCreateAPIView
urlpatterns = [
    path("user-info/",UserRetrieveUpdateAPIView.as_view(), name="user-info"),
    path("register/", UserRegisterCreateAPIView.as_view(), name="register")
]
