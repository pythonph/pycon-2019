from rest_framework import serializers

from pycon.speakers.models import Speaker


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
        )

    def get_image(self, obj):
        return obj.image.url
