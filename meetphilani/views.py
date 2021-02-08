from django.shortcuts import redirect, render
from .forms import MessageModelForm, CollaborationModelForm

# Create your views here.


def home_view(request):
    form = MessageModelForm()
    # submitting form
    if request.method == 'POST':
        form = MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('meetphilani:home')
    return render(request, 'index.html', {
        'form': form,
    })


def about_view(request):
    return render(request, 'about.html', {})


def portfolio_view(request):
    form = CollaborationModelForm()
    if request.method == 'POST':
        form = MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('meetphilani:home')
    return render(request, 'portfolio.html', {'form': form, })


def skills_view(request):
    return render(request, 'services.html', {})
