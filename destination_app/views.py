from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import HireModel,DestinationModel
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# @login_required
def hireform(request):
    if 'id' in request.session:
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            pick_date = request.POST['pick_date']
            full_address = request.POST['full_address']
            phone = request.POST['phone']
            country = request.POST['country']
            tour = request.POST['tour']

            hire = HireModel.objects.create(username=username, email=email, pick_date=pick_date, full_address=full_address, phone=phone,country=country, tour=tour)
            hire.save()
            try:
                send_mail('Hello from Book My Guide',
                'Hello! You have been asked to review the information and confirm or deny the request within 24',
                'bookmyguide1@gmail.com',
                ['dorsh78@gmail.com', 'kalinchowk98@gmail.com'],
                fail_silently = False)
                messages.success(request, 'Hire request sent')
                return redirect('destination:richa')

                # return redirect('destination:richa')
            except:
                return HttpResponse('failed to send email !')
          
        else:
            return render(request, 'hireform.html')
    else:
        return redirect('user:login')

def findaguide(request):
    return render(request, 'findaguide.html')

def annapurna(request):
    return render(request, 'annapurna.html')

def everest(request):
    return render(request, 'everest.html')

def kathmandu(request):
    return render(request, 'kathmandu.html')

def bhaktapur(request):
    return render(request, 'bhaktapur.html')

def trekandtour(request):
    if request.method == "POST":
        qs = DestinationModel.objects.all()
        name_query = request.GET.get('name')

        if name_query != '' and name_query is not None:
            qs = qs.filter(destination__icontains = name_query)

        context= {
            'queryset' : qs
        }
        return render(request, 'trekandtour.html', context)
    else:
        qs = DestinationModel.objects.all()
        context= {
            'queryset' : qs
        }

        return render(request, 'trekandtour.html', context)

def tour(request):
    return render(request, 'tour.html')

def richa(request):
    return render(request, 'richa.html')

def anna(request):
    return render(request, 'anna1.html')
