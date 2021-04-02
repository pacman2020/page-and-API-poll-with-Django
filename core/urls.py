from django.urls import path
from .views import home, list_survey


urlpatterns = [
    path('', home, name='home'),
    path('surveys/', list_survey, name='list-surveys'),
]
