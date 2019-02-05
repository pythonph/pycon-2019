from adminsortable.models import SortableMixin
from django.db import models

from pycon.core.models import Audit


class SponsorType(SortableMixin, Audit):
    name = models.CharField(max_length=64)
    sort_position = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
    )

    class Meta:
        ordering = ['sort_position']

    def __str__(self):
        return self.name


class Sponsor(SortableMixin, Audit):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/sponsor')
    link = models.URLField(blank=True)
    sponsor_type = models.ForeignKey(
        SponsorType,
        on_delete=models.CASCADE,
    )
    sort_position = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
    )

    class Meta:
        ordering = ['sort_position']

    def __str__(self):
        return self.name
