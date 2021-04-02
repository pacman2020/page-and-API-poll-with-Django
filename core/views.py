from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import Survey

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            # new_survey = form.
            form.save()
        return redirect('home')
    forms = SurveyForm()
    return render(request, 'core/home.html', {'forms':forms})

def list_survey(request):
    surveys = Survey.objects.all()
    return render(request, 'core/list-survey.html', {'surveys':surveys})