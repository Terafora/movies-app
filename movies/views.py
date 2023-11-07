from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'movies': [
            'Blade Runner 2049',
            'Glory',
            'The Matrix',
            'Millenium Actress'
        ]
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html')