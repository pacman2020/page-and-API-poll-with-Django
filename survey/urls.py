from django.contrib import admin
from django.urls import path, include

# from core.ApiViewsSet.views import SurveyView
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'api/', SurveyView, basename='Survey')


urlpatterns = [
    path('', include("core.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
