from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegiterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        sz = RegisterUserSerializer(data = data)
        if sz.is_valid():
            user = sz.save()
            refresh = RefreshToken.for_user(user)
            return Response({"message" : "User created succesfully!","access" : str(refresh.access_token), "refresh" : str(refresh)}, status=status.HTTP_201_CREATED)
        return Response({"errors" : sz.errors}, status=status.HTTP_400_BAD_REQUEST)