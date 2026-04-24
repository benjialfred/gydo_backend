from rest_framework import serializers
from .models import Project, Repository

class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ('id', 'git_url', 'default_branch', 'created_at')

class ProjectSerializer(serializers.ModelSerializer):
    repository = RepositorySerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'slug', 'description', 'visibility', 'owner_user', 'owner_team', 'created_at', 'updated_at', 'repository')
        read_only_fields = ('owner_user', 'owner_team', 'slug')

    def create(self, validated_data):
        user = self.context['request'].user
        # Autogenerate simple slug (this should be more robust in prod)
        slug = validated_data['title'].lower().replace(' ', '-')
        project = Project.objects.create(slug=slug, owner_user=user, **validated_data)
        # Create default empty repository
        Repository.objects.create(project=project)
        return project
