from django.urls import path
from core.ApiView.views import SurveyGet, SurveyView
from .views import (
    filter_languagens,
    home, 
    list_survey, 
    deyail_survey, 
    update_survey,
    delete_survey)


urlpatterns = [
    path('', home, name='home'),
    path('surveys/', list_survey, name='list-surveys'),
    path('filter-language/<str:language>/', filter_languagens, name='filter-language'),
    path('<int:pk>/', deyail_survey, name='detail-survey'),
    path('update/<int:pk>/', update_survey, name='update-survey'),
    path('delete/<int:pk>/', delete_survey, name='delete-survey'),
    path('api/', SurveyView.as_view()),
    path('api/<int:pk>', SurveyGet.as_view()),
]
