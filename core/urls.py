from django.urls import path
from .views import (
    home, 
    list_survey, 
    deyail_survey, 
    update_survey)


urlpatterns = [
    path('', home, name='home'),
    path('surveys/', list_survey, name='list-surveys'),
    path('/<int:pk>/', deyail_survey, name='detail-survey'),
    path('update/<int:pk>/', update_survey, name='update-survey'),
]
