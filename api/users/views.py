from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializer import UserSerializer, RegisterUserSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserRegisterCreateAPIView(CreateAPIView):
    serializer_class = RegisterUserSerializer


class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            response = Response(
                {
                    "user": UserSerializer(user).data,
                },
                status=status.HTTP_200_OK,
            )
            response.set_cookie(
                key="access_token",
                value=access,
                httponly=True,
                secure=True,
                samesite="Strict",
            )
            response.set_cookie(
                key="refresh_token",
                value=str(refresh),
                httponly=True,
                secure=True,
                samesite="Strict",
            )
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refrsh_token")
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception as e:
                return Response(
                    {"error": "Error in validating token " + str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            response = Response(
                {"message": "Sucessfully Logout"}, status=status.HTTP_200_OK

            )
            response.delete_cookie('refresh_token')
            response.delete_cookie('access_token')
            return response
