from django.shortcuts import render, HttpResponse
from datetime import datetime   # importing the class date time
from Home.models import Contact      # importing the class contact from our model
from Home.models import LogIns
from django.contrib import messages
from .serials import *
# from django.views.decorators.csrf import csrf_exempt    to bypass the security of csrf token!

# Create your views here.


def index(request):
    # context = { "variable1" : "AMAN BHAI", "variable2" : "SHUKLA JI" }
    return render(request, 'index.html')
    # return render(request, 'index2.html', context)
    # return HttpResponse("This is Home Page")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about Page")


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is Services Page")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # dictionary
        phone = request.POST.get('phone')  # dictionary
        email = request.POST.get('email')  # dictionary
        desc = request.POST.get('desc')  # dictionary
        # creating a object of that contact where name = name , email = email, .,,,,,,
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your contacts has been saved!")
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact Page")

# @csrf_exempt   for csrf import


def LogIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # dictionary
        password = request.POST.get('password')  # dictionary

    q = LogIns.objects.filter(username=username, password=password)
    print(q)
    if q.count() == 0:
        messages.success(request, "Your username or password is incorrect!")
        return render(request, "index.html")
    messages.success(request, "Your LogIn is Successful!")
    return render(request, 'index.html')


def LOGIN(request):
    return render(request, 'real.html')
