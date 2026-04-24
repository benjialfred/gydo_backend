from django.db import models
from django.conf import settings
from teams.models import Team

class Project(models.Model):
    VISIBILITY_CHOICES = [
        ('PUBLIC', 'Public'),
        ('PRIVATE', 'Private'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='PRIVATE')
    
    owner_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='owned_projects')
    owner_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='projects')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Repository(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='repository')
    git_url = models.CharField(max_length=255, blank=True, help_text="Internal bare git repo path or external URL")
    default_branch = models.CharField(max_length=50, default='main')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Repo for {self.project.title}"

class ProjectFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    path = models.CharField(max_length=500, help_text="File path e.g., src/main.js")
    content = models.TextField(blank=True)
    is_directory = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('project', 'path')

    def __str__(self):
        return self.path
