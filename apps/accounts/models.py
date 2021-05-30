from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name=_('username'),
        max_length=60,
        unique=True
    )
    email = models.EmailField(
        verbose_name=_('email'),
        unique=True
    )
    is_staff = models.BooleanField(
        verbose_name=_('is staff'),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_('is active'),
        default=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_('date joined'),
        default=timezone.now
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
