from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializer import UserSerializer,RegisterUserSerializer

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes =[IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
    

class UserRegisterCreateAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer