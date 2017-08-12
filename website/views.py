from django.shortcuts import render

# Create your views here.

def homepage(request):
    context = {}
    if request.is_ajax():
        reserveData = {}
        reserveData['clientName'] = request.POST['clientName']
        reserveData['phoneNumber'] = request.POST['phoneNumber']
        context['reserveData'] = reserveData
        return render(request, 'reserveresponse.html', context)
        pass;
    else:
        return render(request, 'homepage.html', context)
