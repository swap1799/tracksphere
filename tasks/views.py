from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from projects.models import Project
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied

# Create your views here.


User = get_user_model()

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            project__organization = self.request.user.organization
        )
    
    def perform_create(self, serializer):
        user = self.request.user
        project = serializer.validated_data.get("project")
        assigned_to = serializer.validated_data.get("assigned_to")

        # Check project belongs to same organization
        if project.organization != user.organization:
            raise PermissionDenied("You cannot create tasks in another organization.")
        
        # Check assigned user belongs to same organization
        if assigned_to and assigned_to.organization != user.organization:
            raise PermissionDenied("Cannot assign task to user from another organization.")

        serializer.save()
    