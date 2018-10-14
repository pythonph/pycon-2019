from django.db import models

from core.models import UserAudit

# Create your models here.


class Proposal(UserAudit):

    BEGINNER = 'beginner'
    ADVANCE = 'advance'
    EXPERT = 'expert'

    AUDIENCE_LEVEL_CHOICES = (
        (BEGINNER, 'Beginner'),
        (ADVANCE, 'Advance'),
        (EXPERT, 'Expert'),
    )

    TALK = 'talk'
    WORKSHOP = 'workshop'
    PANEL = 'panel'

    PRESENTATION_TYPE_CHOICES = (
        (TALK, 'Talk'),
        (WORKSHOP, 'Workshop'),
        (PANEL, 'Panel')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    abstract = models.TextField()
    audience_level = models.CharField(
        max_length=30,
        choices=AUDIENCE_LEVEL_CHOICES
    )
    presentation_type = models.CharField(
        max_length=30,
        choices=PRESENTATION_TYPE_CHOICES
    )
    duration = models.DurationField()

    def __str__(self):
        return self.title
