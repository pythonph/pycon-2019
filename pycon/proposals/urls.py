from django.urls import path

from .views import (
    ProposalCreateView
)


app_name = 'proposals'
urlpatterns = [
    path('add/', ProposalCreateView.as_view(), name='create_proposal'),
]
