from django.urls import path
from .views import RegiterView
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path("login/",TokenObtainPairView.as_view()),
    path("register/", RegiterView.as_view())
]
