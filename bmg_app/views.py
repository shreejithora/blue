from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ourservices(request):
    return render(request, 'ourservices.html')

def whyus(request):
    return render(request, 'whyus.html')

def store(request):
    return render(request, 'store.html')

def sendmail(request):
    if request.method == "GET":
        # name = request.POST.get('username')
        # email = request.POST.get('email')
        print(request.GET.get('username'))
        try:
            send_mail('Hello from Book My Guide',
            'Hello! You have been asked to review the information and confirm or deny the request within 24',
            'bookmyguide1@gmail.com',
            ['dorsh78@gmail.com', 'kalinchowk98@gmail.com'],
            fail_silently = False)
            return redirect('destination:richa')
        except:
            return HttpResponse('failed to send email !')
    else:
        return redirect('destination:richa')
