from django.db import models

from pycon.core.models import Audit

# Create your models here.


class Speaker(Audit):
    NORMAL = 'n'
    KEYNOTE = 'k'
    CHOICES = (
        (NORMAL, 'Normal'),
        (KEYNOTE, 'Keynote')
    )
    name = models.CharField(max_length=64)
    company_name = models.CharField(max_length=128, blank=True, null=True)
    job_title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/speaker')
    speaker_type = models.CharField(
        max_length=1,
        default=NORMAL,
        choices=CHOICES
    )

    def __str__(self):
        return self.name
