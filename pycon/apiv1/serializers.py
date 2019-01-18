from rest_framework import serializers

from pycon.speakers.models import Speaker
from pycon.sponsors.models import Sponsor, SponsorType


class SpeakerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Speaker
        fields = (
            'id',
            'name',
            'company_name',
            'job_title',
            'description',
            'image',
            'github',
            'facebook',
            'twitter',
        )

    def get_image(self, obj):
        return obj.image.url


class SponsorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Sponsor
        fields = (
            'name',
            'description',
            'image',
            'link',
        )

    def get_image(self, obj):
        return obj.image.url


class SponsorTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SponsorType
        fields = (
            'id',
            'name'
        )
