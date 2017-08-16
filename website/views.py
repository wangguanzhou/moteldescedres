from django.shortcuts import render
from .forms import *

# Create your views here.

def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)

def reserve(request):
    context = {}
    if request.POST:
        reserveForm = ReserveForm(request.POST)
        context['reserveForm'] = reserveForm

        return render(request, 'reserveresponse.html', context)

    else:
        reserveForm = ReserveForm()
        context['reserveForm'] = reserveForm
        return render(request, 'reserve.html', context)
