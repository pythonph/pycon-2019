from rest_framework.generics import ListAPIView

from .serializers import (
    SpeakerSerializer,
    SponsorSerializer,
    SponsorTypeSerializer,
)
from pycon.speakers.models import Speaker
from pycon.sponsors.models import Sponsor, SponsorType

# Create your views here.

class KeynoteListAPIView(ListAPIView):

    model = Speaker
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        return self.model.objects.filter(
            speaker_type=Speaker.KEYNOTE
        )

class NormalSpeakerListAPIView(ListAPIView):

    model = Speaker
    serializer_class = SpeakerSerializer

    def get_queryset(self):
        return self.model.objects.filter(
            speaker_type=Speaker.NORMAL
        )


class SponsorListAPIView(ListAPIView):

    model = Sponsor
    serializer_class = SponsorSerializer

    def get_queryset(self):
        return self.model.objects.filter(
            sponsor_type_id=self.kwargs['sponsor_type_id']
        )


class SponsorTypeListAPIView(ListAPIView):

    model = SponsorType
    serializer_class = SponsorTypeSerializer

    def get_queryset(self):
        return self.model.objects.all()
