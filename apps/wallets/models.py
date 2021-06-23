import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseDatetimeModelMixin, UUIDModelMixin


class Entity(BaseDatetimeModelMixin, UUIDModelMixin, models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=30
    )
    code = models.CharField(
        verbose_name=_('code'),
        max_length=3,
        unique=True
    )
    country = models.ForeignKey(
        'countries.Country',
        verbose_name=_('country'),
        related_name='entities',
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self

    class Meta:
        verbose_name = _('entity')
        verbose_name_plural = _('entities')


class Wallet(BaseDatetimeModelMixin, UUIDModelMixin, models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=30
    )
    entity = models.ForeignKey(
        'wallets.Entity',
        verbose_name=_('entity'),
        related_name='wallets',
        on_delete=models.DO_NOTHING
    )
    currency = models.ForeignKey(
        'countries.Currency',
        verbose_name=_('currency'),
        related_name='wallets',
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self

    class Meta:
        verbose_name = _('wallet')
        verbose_name_plural = _('wallets')
