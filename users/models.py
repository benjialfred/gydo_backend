from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_2fa_enabled = models.BooleanField(default=False)
    totp_secret = models.CharField(max_length=255, blank=True, null=True)
    wallet_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
