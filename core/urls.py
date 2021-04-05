from django.urls import path
from .views import (
    home, 
    list_survey, 
    deyail_survey, 
    update_survey,
    delete_survey)


urlpatterns = [
    path('', home, name='home'),
    path('surveys/', list_survey, name='list-surveys'),
    path('<int:pk>/', deyail_survey, name='detail-survey'),
    path('update/<int:pk>/', update_survey, name='update-survey'),
    path('delete/<int:pk>/', delete_survey, name='delete-survey'),
]
