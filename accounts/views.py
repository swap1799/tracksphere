from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer, OrganizationTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class OrganizationTokenObtainPairView(TokenObtainPairView):
    serializer_class = OrganizationTokenObtainPairSerializer
