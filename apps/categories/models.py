import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.models import BaseDatetimeModelMixin, UUIDModelMixin


class Label(BaseDatetimeModelMixin, UUIDModelMixin, models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=30
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self

    class Meta:
        verbose_name = _('label')
        verbose_name_plural = _('labels')


class Type(BaseDatetimeModelMixin, UUIDModelMixin, models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=30
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self

    class Meta:
        verbose_name = _('type')
        verbose_name_plural = _('types')


class Category(BaseDatetimeModelMixin, UUIDModelMixin, models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=30
    )
    type = models.ForeignKey(
        'categories.Type',
        verbose_name=_('type'),
        related_name='categories',
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
