from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        return 'save'
    return render(request, 'core/home.html')