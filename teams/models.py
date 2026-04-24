from django.db import models
from django.conf import settings

class Team(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Membership(models.Model):
    ROLE_CHOICES = [
        ('OWNER', 'Owner'),
        ('MAINTAINER', 'Maintainer'),
        ('CONTRIBUTOR', 'Contributor'),
        ('VIEWER', 'Viewer'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='memberships')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='memberships')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='VIEWER')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'team')

    def __str__(self):
        return f"{self.user.email} - {self.team.name} ({self.role})"
