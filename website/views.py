from django.shortcuts import render
from django.core.mail import send_mail
import urllib
from urllib.request import urlopen
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

        smsNotification = 'There is a new reservation via moteldescedres.ca. Please check your email.'
        sendSMSviaNexmo(smsNotification)


        return render(request, 'reserveresponse.html', context)

    else:
        reserveForm = ReserveForm()
        context['reserveForm'] = reserveForm
        return render(request, 'reserve.html', context)


def showrooms(request):
    return render(request, 'rooms.html', {})


def sendSMSviaNexmo(smsContent):
    params = {
            'api_key': '8f27294a',
            'api_secret': 'f44647eee9a437f0',
            'to': '15147757799',
            'from': '12264063982',
            'text': smsContent
            }

    url = 'https://rest.nexmo.com/sms/json?' + urllib.parse.urlencode(params)
    request = urllib.request.Request(url)
    request.add_header('Accept', 'application/json')
    response = urllib.request.urlopen(request)
    if response.code == 200 :
        print('SMS notification success')
    else:
        print('SMS notification failure')

