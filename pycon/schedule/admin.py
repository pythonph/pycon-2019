from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline
from django.contrib import admin

from .models import Event, ProgramSchedule


class EventInline(SortableStackedInline):
    model = Event
    extra = 1


class ProgramScheduleAdmin(NonSortableParentAdmin):
    inlines = [EventInline]


admin.site.register(ProgramSchedule, ProgramScheduleAdmin)
