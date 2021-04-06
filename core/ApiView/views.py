from rest_framework.response import Response
from core.models import Survey
from .serializers import SerializeSurvey
from rest_framework.views import APIView
from django.http import Http404


class SurveyView(APIView):
    def get(self, request, format=None):
        surveys = Survey.objects.all()
        serializer = SerializeSurvey(surveys, many=True)
        return Response(serializer.data)

class SurveyGet(APIView):
    def get_object(self, pk):
        try:
            return Survey.objects.get(pk=pk)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = SerializeSurvey(survey)
        return Response(serializer.data)