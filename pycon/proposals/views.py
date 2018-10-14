from django.views.generic.edit import CreateView

from .models import Proposal
# Create your views here.


class ProposalCreateView(CreateView):
    model = Proposal
    fields = [
        'title',
        'description',
        'abstract',
        'audience_level',
        'presentation_type',
        'duration'
    ]
    template_name = 'proposals/create_proposal.html'
