from django.contrib import admin

from .models import Proposal
from core.admin import AuditModelAdmin

# Register your models here.


class ProposalAdmin(AuditModelAdmin):

    list_display = (
        'id',
        'title',
        'is_active'
    )

admin.site.register(Proposal, ProposalAdmin)
