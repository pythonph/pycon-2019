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
    success_url = '/'
    template_name = 'proposals/create_proposal.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ProposalCreateView, self).form_valid(form)
