from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterView, OrganizationTokenObtainPairView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', OrganizationTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]