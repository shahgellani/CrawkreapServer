from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from emailparser.models import Emails
from emailparser.serializers import EmailSerializer


class EmailListView(generics.ListAPIView):
    # specify the model for list view
    model = Emails
    serializer_class = EmailSerializer
    queryset = Emails.objects.all()
