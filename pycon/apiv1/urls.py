from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    KeynoteListAPIView,
    NormalSpeakerListAPIView,
    SponsorListAPIView,
    SponsorTypeListAPIView,
)

speaker_patterns = format_suffix_patterns([
    path(
        'keynote/list/',
        KeynoteListAPIView.as_view(),
        name='keynote_list'
    ),
    path(
        'normal/list/',
        NormalSpeakerListAPIView.as_view(),
        name='normal_list'
    ),
])

sponsor_patterns = format_suffix_patterns([
    path(
        'type/list/',
        SponsorTypeListAPIView.as_view(),
        name='sponsor_type_list'
    ),
    path(
        '<int:sponsor_type_id>/list/',
        SponsorListAPIView.as_view(),
        name='sponsor_list'
    ),
])

app_name = 'apiv1'
urlpatterns = [
    path('speakers/', include(speaker_patterns)),
    path('sponsors/', include(sponsor_patterns))
]
