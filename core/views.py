from django.shortcuts import render, redirect, get_object_or_404
from .forms import SurveyForm
from .models import Survey


#filros survey
#update
#delete
#priva rotas deletar, update, list, detail

def home(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
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
    
def update_survey(request, pk):
    survey = get_object_or_404(Survey,pk=pk)
    
    if request.method == 'POST':
        form = SurveyForm(request.POST, instance=survey)
        if form.is_valid():
            # new_survey = form.
            form.save()
        return redirect('detail-survey',  pk=survey.pk)
    
    forms = SurveyForm(instance=survey)
    return render(request, 'core/update-survey.html', {'forms':forms})

def delete_survey(request, pk):
    survey = get_object_or_404(Survey,pk=pk)
    
    if survey:
        survey.delete()
        return redirect('list-surveys')
    return redirect('detail-survey',  pk=survey.pk)
