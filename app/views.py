from django.shortcuts import render,redirect
from app.models import LandingFormModel
from django.contrib import messages
from django.core.mail import send_mail
from LandingPage import settings as se
# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def landingFormSave(request):
    fname=request.POST['firstname']
    lname=request.POST['lastname']
    email=request.POST['email']
    number=request.POST['mobilenumber']
    message=request.POST['message']
    print(fname)
    l=LandingFormModel(firstname=fname,lastname=lname,emailid=email,mobile=number,message=message)
    l.save()
    messages.success(request, 'Form submitted successfully.')
    mail=send_mail('landingpage',message,'mounika.kandikattu10@gmail.com',['mounika.kandikattu10@gmail.com'])
    return redirect('index' )