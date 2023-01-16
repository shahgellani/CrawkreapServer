from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User , UserProfile
from .serializers import RegisterSerializer
from .utils.token_manager import get_tokens_for_user


class UserViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = User.objects.all()


class LoginView(APIView):
    """
    Login View

    """

    def post(self, request):
        """

        :param request:
        :return: Tokens , User, Message
        """
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
            data = {"auth_data": auth_data, "user": ""}
            return Response(
                {"msg": "Login Success", **auth_data}, status=status.HTTP_200_OK
            )
        return Response(
            {"msg": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class UserSignUp(APIView):
    """
    User signup view
    """
    authentication_classes = []
    response_dict = {}

    def post(self, request):
        """
        For creating new user
        :param request:
        :return:
        """
        try:
            validated_data = RegisterSerializer(data=request.data)
            if validated_data.is_valid():
                RegisterSerializer.create(validated_data=validated_data)
                self.response_dict["msg"] = validated_data.data
                self.response_dict["response_status"] = True
            else:
                self.response_dict["msg"] = validated_data.errors
                self.response_dict["response_status"] = True
        except Exception as e:
            self.response_dict["msg"] = str(e)
            self.response_dict["response_status"] = False
        finally:
            return Response(
                self.response_dict
            )
