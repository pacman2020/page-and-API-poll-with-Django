from django.urls import path
from .views import home, list_survey, deyail_survey


urlpatterns = [
    path('', home, name='home'),
    path('/<int:pk>/', deyail_survey, name='detail-survey'),
    path('surveys/', list_survey, name='list-surveys'),
]
