import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseDatetimeModelMixin, UUIDModelMixin


class Profile(BaseDatetimeModelMixin, UUIDModelMixin, models.Model):
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=30
    )
    middle_name = models.CharField(
        verbose_name=_('middle name'),
        max_length=30,
        default='',
        blank=True
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=60,
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='profile',
        on_delete=models.DO_NOTHING
    )
    labels = models.ManyToManyField(
        'categories.Label',
        through='profiles.ProfileLabel',
        related_name='labels',
        blank=True
    )
    categories = models.ManyToManyField(
        'categories.Category',
        through='profiles.ProfileCategory',
        related_name='categories',
        blank=True
    )

    def __str__(self):
        return self.get_full_name()

    def __unicode__(self):
        return self

    def get_full_name(self):
        full_name = f'{self.first_name} {self.middle_name} {self.last_name}'
        return full_name.replace('  ', ' ')
    
    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')


class ProfileLabel(BaseDatetimeModelMixin, UUIDModelMixin, models.Model):
    profile = models.ForeignKey(
        'profiles.Profile',
        verbose_name=_('profile'),
        related_name='profile_labels',
        on_delete=models.DO_NOTHING
    )
    label = models.ForeignKey(
        'categories.Label',
        verbose_name=_('label'),
        related_name='profile_labels',
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f'{self.profile} {self.label}'

    def __unicode__(self):
        return self

    class Meta:
        verbose_name = _('profile label')
        verbose_name_plural = _('profile labels')


class ProfileCategory(BaseDatetimeModelMixin, UUIDModelMixin, models.Model):
    profile = models.ForeignKey(
        'profiles.Profile',
        verbose_name=_('profile'),
        related_name='profile_categories',
        on_delete=models.DO_NOTHING
    )
    category = models.ForeignKey(
        'categories.Category',
        verbose_name=_('category'),
        related_name='profile_categories',
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f'{self.profile} {self.category}'

    def __unicode__(self):
        return self

    class Meta:
        verbose_name = _('profile category')
        verbose_name_plural = _('profile categories')
