import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseDatetimeModelMixin, UUIDModelMixin


class Profile(BaseDatetimeModelMixin, UUIDModelMixin, models.Model):
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=30,
        blank=False,
        null=False
    )
    middle_name = models.CharField(
        verbose_name=_('middle name'),
        max_length=30,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=60,
        blank=False,
        null=False
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='profile',
        blank=False,
        null=False,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __unicode__(self):
        return self
