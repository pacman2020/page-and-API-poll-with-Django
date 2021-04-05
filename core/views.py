from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SurveyForm
from .models import Survey
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#filros survey
#priva rotas deletar, update, list, detail

def home(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    forms = SurveyForm()
    return render(request, 'core/home.html', {'forms':forms})

@login_required
def list_survey(request):
    surveys = Survey.objects.all()
    
    #criando filtro apenas de language escolhidas
    filter_language = []
    for l in surveys:
        if not l.language in filter_language:
            filter_language.append(l.language)
    
    if request.method == 'POST':
        search = request.POST.get('search')
        language = request.POST.get('language')
        
        if language:
            surveys = Survey.objects.filter(language=language)
                    
            paginator = Paginator(surveys, 100)
            page = request.GET.get('page')
            data = {
                'surveys': paginator.get_page(page),
                'all_surveys': len(surveys),
                'filter_language': filter_language
                }
            return render(
                request, 'core/list-survey.html', 
                data)
        
        if search:
            surveys = Survey.objects.filter(full_name=search)
            
            paginator = Paginator(surveys, 100)
            page = request.GET.get('page')
            data = {
                'surveys': paginator.get_page(page),
                'all_surveys': len(surveys),
                'filter_language': filter_language
                }
            return render(
                request, 'core/list-survey.html', 
                data)
    
    paginator = Paginator(surveys, 10)
    page = request.GET.get('page')
    data = {
        'surveys': paginator.get_page(page),
        'all_surveys': len(surveys),
        'filter_language': filter_language
        }
    return render(
        request, 'core/list-survey.html', 
        data)

@login_required
def deyail_survey(request, pk):
    survey = get_object_or_404(Survey,pk=pk)
    
    return render(
        request, 'core/detail-survey.html', 
        {'survey':survey })
 
@login_required    
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

@login_required
def delete_survey(request, pk):
    survey = get_object_or_404(Survey,pk=pk)
    
    if survey:
        survey.delete()
        return redirect('list-surveys')
    return redirect('detail-survey',  pk=survey.pk)
