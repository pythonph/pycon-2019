from adminsortable.models import SortableMixin
from django.db import models


class ProgramSchedule(models.Model):
    LEFT = 'lef'
    RIGHT = 'rig'
    TAB_POSITION_CHOICES = (
        (LEFT, 'Left'),
        (RIGHT, 'Right'),
    )

    name = models.CharField(
        max_length=255,
        help_text='e.g. Day 1 (February 24)',
    )
    tab_position = models.CharField(
        choices=TAB_POSITION_CHOICES,
        default=LEFT,
        max_length=3,
        unique=True,
    )

    def __str__(self):
        return self.name


class Event(SortableMixin):
    title = models.CharField(
        help_text='Title of the event.',
        max_length=255,
    )
    subtitle = models.CharField(
        blank=True,
        help_text='If provided, appears below the event title.',
        max_length=255,
    )
    description = models.TextField(
        blank=True,
        help_text='Description of the event.'
    )
    start_time = models.TimeField(
        help_text='Start time of the event.',
    )
    end_time = models.TimeField(
        help_text='End time of the event.',
    )
    venue = models.CharField(
        blank=True,
        help_text='Room or venue where this event will be held.',
        max_length=255,
    )

    program = models.ForeignKey(
        'schedule.ProgramSchedule',
        on_delete=models.CASCADE,
        related_name='events',
    )

    sort_position = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
    )

    class Meta:
        ordering = ['sort_position']

    def __str__(self):
        return self.title

    @property
    def time_display(self):
        time_format = '%-I:%M %p'
        start_time = self.start_time.strftime(time_format)
        end_time = self.end_time.strftime(time_format)
        return '{start_time} – {end_time}'.format(
            start_time=start_time, end_time=end_time
        )
