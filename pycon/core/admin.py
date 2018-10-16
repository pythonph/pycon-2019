from django.contrib import admin

# Register your models here.

class AuditModelAdmin(admin.ModelAdmin):

    list_filter = (
        'created_time',
        'modified_time',
        'is_active'
    )
