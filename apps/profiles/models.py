import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

<<<<<<< HEAD
from apps.utils.models import BaseDatetimeModelMixin, UUIDModelMixin


class Profile(BaseDatetimeModelMixin, UUIDModelMixin, models.Model):
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=30
=======

class Profile(models.Model):
    uuid = models.UUIDField(
        verbose_name=_('uuid'),
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=30,
        blank=False,
        null=False
>>>>>>> 4b6ed126233285efef0f86abd3ff9e8b1ab2988f
    )
    middle_name = models.CharField(
        verbose_name=_('middle name'),
        max_length=30,
<<<<<<< HEAD
        default='',
        blank=True
=======
        blank=True,
        null=True
>>>>>>> 4b6ed126233285efef0f86abd3ff9e8b1ab2988f
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=60,
<<<<<<< HEAD
=======
        blank=False,
        null=False
>>>>>>> 4b6ed126233285efef0f86abd3ff9e8b1ab2988f
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='profile',
<<<<<<< HEAD
=======
        blank=False,
        null=False,
>>>>>>> 4b6ed126233285efef0f86abd3ff9e8b1ab2988f
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
<<<<<<< HEAD
        return self.get_full_name()

    def __unicode__(self):
        return self

    def get_full_name(self):
        full_name = f'{self.first_name} {self.middle_name} {self.last_name}'
        return full_name.replace('  ', ' ')
    
    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
=======
        return f'{self.first_name} {self.last_name}'

    def __unicode__(self):
        return self
>>>>>>> 4b6ed126233285efef0f86abd3ff9e8b1ab2988f
