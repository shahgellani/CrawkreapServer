from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.readEmail import ReadEmail
from .models import User
from .serializers import UserSerializer
from .utils.token_manager import get_tokens_for_user


class UserViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    """

    """
    def post(self, request):
        """

        :param request:
        :return: Tokens , User, Message
        """
        ReadEmail.read_email()
        if "email" not in request.data or "password" not in request.data:
            return Response(
                {"msg": "Credentials missing"}, status=status.HTTP_400_BAD_REQUEST
            )
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            data = {"auth_data" :auth_data , "user" : "" }
            return Response(
                {"msg": "Login Success", **auth_data}, status=status.HTTP_200_OK
            )
        return Response(
            {"msg": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )

