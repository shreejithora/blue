from django.shortcuts import render, redirect
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256
from .models import GuideRegisterModel, TouristRegisterModel, LanguageModel

# Create your views here.

def loginauth(request):
    if request.method == "POST":
        e = request.POST.get('email')
        p = request.POST.get('password')
        guide = GuideRegisterModel.objects.filter(email=e, password=p)
        tourist = TouristRegisterModel.objects.filter(email=e, password=p)
        if(guide.count() > 0 or tourist.count() > 0 ):
                for user in guide:
                    request.session['email'] = user.email
                    request.session['id'] = user.id
                    request.session['username'] = user.username

                for user in tourist:
                    request.session['email'] = user.email
                    request.session['id'] = user.id
                    request.session['username'] = user.username

                return redirect('destination:findaguide')
        else:
            return HttpResponse('Wrong Credentials')
    else:
        return render(request, 'login.html')

def signup_guide(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        bio_desc = request.POST['bio_desc']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        gender = request.POST['gender']
        address = request.POST['address']
        phone = request.POST['phone']
        user_img = request.POST['user_img']
        citizenship_img = request.POST['citizenship_img']
        liscence_img = request.POST['Liscence_img']
        languages = request.POST['languages']
        locations = request.POST['locations']

        enc_password = pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)

        # lan = LanguageModel.objects.filter(language__in=languages)
        guide = GuideRegisterModel.objects.create(first_name=first_name, last_name=last_name, username=username, bio_desc=bio_desc, email=email, password=enc_password, gender=gender, address=address, phone=phone, user_img=user_img, citizenship_img=citizenship_img, Liscence_img=liscence_img,languages=languages, locations=locations)
        # guide.languages.set(language)
        guide.save()
       
        return redirect('user:login')

    else:
        return render(request, 'signup_guide.html')

def signup_tourist(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        gender = request.POST['gender']

        enc_password = pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)

        tourist = TouristRegisterModel.objects.create(username=username, email=email, password=enc_password, gender=gender)
        tourist.save()
        return redirect('user:login')
    else:
        return render(request, 'signup_tourist.html')

def logout(request):
    request.session.flush()
    return redirect('bmg_app:home')
