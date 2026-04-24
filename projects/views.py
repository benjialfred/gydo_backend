from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer
from django.db.models import Q

class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Return projects owned by user or where project is public
        return Project.objects.filter(Q(owner_user=user) | Q(visibility='PUBLIC'))

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(Q(owner_user=user) | Q(visibility='PUBLIC'))
