from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse, response, Http404
from .forms import MessageModelForm, CollaborationModelForm
from .models import FileAdmin

import os

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
        'file': FileAdmin.objects.all()
    })


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response

    raise Http404


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
