from django.contrib import admin

# Register your models here.
from .models import Speaker

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'speaker_type')

admin.site.register(Speaker, SpeakerAdmin)
