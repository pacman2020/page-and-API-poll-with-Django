from django.shortcuts import render, redirect, get_object_or_404
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
    
    return render(
        request, 'core/list-survey.html', 
        {'surveys':surveys, 'all_surveys': len(surveys)})

def deyail_survey(request, pk):
    survey = get_object_or_404(Survey,pk=pk)
    
    return render(
        request, 'core/detail-survey.html', 
        {'survey':survey })
    
