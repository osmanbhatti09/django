from django.shortcuts import render 
from django.http import HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    'city' : {'Colradou'}
    message.sucess(request, "this is a test message")
    return render(request, 'index.html')

    #return httpResponse(request, 'Hello this is world')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Profile details updated.')

    return httpResponse(request, 'show about page here')    