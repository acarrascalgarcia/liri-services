import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseDatetimeModelMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now=False,
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        auto_now_add=False
    )

    class Meta:
        abstract = True


class UUIDModelMixin(models.Model):
    uuid = models.UUIDField(
        verbose_name=_('uuid'),
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    class Meta:
        abstract = True
