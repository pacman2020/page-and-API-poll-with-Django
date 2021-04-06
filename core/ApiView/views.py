from rest_framework.response import Response
from core.models import Survey
from .serializers import SerializeSurvey
from rest_framework.views import APIView


class SurveyView(APIView):
    def get(self, request, format=None):
        surveys = Survey.objects.all()
        serializer = SerializeSurvey(surveys, many=True)
        return Response(serializer.data)
