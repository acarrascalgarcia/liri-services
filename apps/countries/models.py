import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseDatetimeModelMixin


class Currency(BaseDatetimeModelMixin, models.Model):
    code = models.CharField(
        verbose_name=_('code'),
        primary_key=True,
        max_length=3
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=15
    )
    english_name = models.CharField(
        verbose_name=_('english name'),
        max_length=60
    )
    symbol = models.CharField(
        verbose_name=_('symbol'),
        max_length=3
    )

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self
    
    class Meta:
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')


class Country(BaseDatetimeModelMixin, models.Model):
    code = models.CharField(
        verbose_name=_('code'),
        primary_key=True,
        max_length=2
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=60
    )
    english_name = models.CharField(
        verbose_name=_('english name'),
        max_length=60
    )
    flag_url = models.URLField(
        verbose_name=_('flag url'),
        max_length=3,
        default='',
        blank=True
    )
    currency = models.ForeignKey(
        'countries.Currency',
        verbose_name=_('currency'),
        related_name='countries',
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self
    
    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')
