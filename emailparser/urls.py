from django.urls import re_path, include, path
from rest_framework import routers

from emailparser.views import EmailListView

router = routers.DefaultRouter()


urlpatterns = [
    path('email-list/', EmailListView.as_view(), name='email_list'),
]
