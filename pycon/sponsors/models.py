from django.db import models

# Create your models here.
from pycon.core.models import Audit


class SponsorType(Audit):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Sponsor(Audit):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/sponsor')
    link = models.URLField()
    sponsor_type = models.ForeignKey(
        SponsorType,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
