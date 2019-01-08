from django.contrib import admin

# Register your models here.
from .models import (
    Sponsor,
    SponsorType,
)

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sponsor_type')

class SponsorTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorType, SponsorTypeAdmin)
