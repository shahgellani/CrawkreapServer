from django.urls import re_path, include, path
from rest_framework import routers
from .views import UserViewSet, LoginView, UserSignUp

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('signup/', UserSignUp.as_view(), name='signup_view'),
    re_path(r'^', include(router.urls)),
    # re_path(r'^auth/', include('rest_auth.urls'))
]