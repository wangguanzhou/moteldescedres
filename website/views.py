from django.shortcuts import render
from django.core.mail import send_mail
from datetime import datetime
import urllib
from urllib.request import urlopen
from django.template.loader import render_to_string
from .forms import *

# Create your views here.

def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)

def reserve(request):
    context = {}
    reserveData = {}
    if request.POST:
        reserveForm = ReserveForm(request.POST)
        if reserveForm.is_valid():
            reserveData['checkin_date'] = reserveForm.cleaned_data['checkin_date'] 
            reserveData['checkout_date'] = reserveForm.cleaned_data['checkout_date'] 
            reserveData['room_type'] = reserveForm.cleaned_data['room_type'] 
            reserveData['num_of_rooms'] = reserveForm.cleaned_data['num_of_rooms'] 
            reserveData['num_of_adults'] = reserveForm.cleaned_data['num_of_adults'] 
            reserveData['num_of_children'] = reserveForm.cleaned_data['num_of_children'] 
            reserveData['client_name'] = reserveForm.cleaned_data['client_name'] 
            reserveData['client_phone'] = reserveForm.cleaned_data['client_phone'] 
            reserveData['client_email'] = reserveForm.cleaned_data['client_email'] 
            reserveData['client_message'] = reserveForm.cleaned_data['client_message'] 
            
            context['reserveData'] = reserveData

            sendReservationEmail(reserveData)

            smsNotification = 'There is a new reservation via moteldescedres.ca. Please check your email.'
            # sendSMSviaNexmo(smsNotification)

        else:
            print('Form error')
        return render(request, 'reserveresponse.html', context)

    else:
        reserveForm = ReserveForm()
        context['reserveForm'] = reserveForm
        return render(request, 'reserve.html', context)


def showrooms(request):
    return render(request, 'rooms.html', {})


def sendReservationEmail(reserveData):
    context = {}
    context['reserveData'] = reserveData

    reserveTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    emailSubject = 'New reservation request from [' + reserveData['client_name'] + '] - ' + reserveTime 
    emailBody = render_to_string('reserve_notification.txt', context)
    emailFrom = 'admin@moteldescedres.ca'
    emailTo1 = 'moteldescedres@videotron.ca'
    emailTo2 = 'alexwang74@gmail.com'

    send_mail(emailSubject, emailBody, emailFrom, [emailTo1, emailTo2], fail_silently =False)

def sendSMSviaNexmo(smsContent):
    params = {
            'api_key': '8f27294a',
            'api_secret': 'f44647eee9a437f0',
            'to': '15145717719',
            'from': '12508006799',
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

