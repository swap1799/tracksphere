from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print('organization:',self.request.user.organization)
        return Project.objects.filter(organization = self.request.user.organization)
    
    def perform_create(self, serializer):
        print('user:',self.request.user)
        serializer.save(organization=self.request.user.organization,created_by=self.request.user)