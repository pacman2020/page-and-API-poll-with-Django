from rest_framework import serializers
from core.models import Survey


class SerializeSurvey(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'