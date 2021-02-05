from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'index.html', {})


def about_view(request):
    return render(request, 'about.html', {})


def portfolio_view(request):
    return render(request, 'portfolio.html', {})


def skills_view(request):
    return render(request, 'services.html', {})
