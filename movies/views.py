from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'movies/index.html', {'movie': 'Blade Runner 2049'})

def about(request):
    return render(request, 'movies/about.html')