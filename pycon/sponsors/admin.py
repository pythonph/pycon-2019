from adminsortable.admin import SortableAdmin, SortableTabularInline
from django.contrib import admin

# Register your models here.
from .models import (
    Sponsor,
    SponsorType,
)


class SponsorInline(SortableTabularInline):
    model = Sponsor
    extra = 1


class SponsorTypeAdmin(SortableAdmin):
    list_display = ('name',)
    inlines = [SponsorInline]


admin.site.register(SponsorType, SponsorTypeAdmin)
