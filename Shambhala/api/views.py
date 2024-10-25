from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Reviews, WeatherData, Address, ContactUs
import requests
import json
import numpy as np
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not (username and email and password):
            return render(request, "api/signup.html", {"error": "All fields are required."})

        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        return redirect('login')
    
    return render(request, "api/signup.html")


# Login view
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("user not none")
            # Redirect to home page after successful login
            return redirect('api/home.html')
        else:
            print("user is none")
            return render(request, "api/login.html", {"error": "Invalid login credentials."})

    return render(request, "api/login.html")


# Landing Page (after login)
def landing_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        # Handling reviews
        name = request.POST.get('full_name')
        review_text = request.POST.get('review')
        if name and review_text:
            new_review = Reviews.objects.create(
                username=name, body=review_text)
            new_review.save()

        # Handling contact us
        contact_name = request.POST.get('contactname')
        contact_email = request.POST.get('contactemail')
        contact_msg = request.POST.get('message')
        if contact_name and contact_email and contact_msg:
            new_contact = ContactUs.objects.create(
                username=contact_name, email=contact_email, message=contact_msg)
            new_contact.save()

    return render(request, "api/home.html")
    

def Review(request):
   return render(request, 'api/reviews.html')

def Weather(request):
  r = request.POST
  print(r)
   
  
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=2696dd3de015ae6c54e56ae12c77b507'
  cities = ['Patiala']
  TempSum=0
  WeatherStatus=[]
  for city in cities:
    Response = requests.get(url.format(city))
    data = eval(Response.text)
    
    print(data)
    
    WeatherStatus.append({str(city) : [str(data['weather'][0]['description']), str(data['main']['humidity']), str(data['wind']['speed'])]})
    TempSum = data['main']['temp']
    # AvgTemp = TempSum/len(cities)
    DictData = {"Weather":WeatherStatus, "Average temperature":TempSum}
    print(DictData)
    FullData = WeatherData.objects.create(JourneyWeather = json.dumps(DictData))
    FullData.save()
    
    return render(request, 'api/weather.html', context={'weather':[str(city),str(data['weather'][0]['description']),str(data['main']['humidity']), str(data['wind']['speed']), TempSum]})





def contact(request):
  return render(request, 'api/contactus.html')


@csrf_exempt
def journey(request):
    if request.method == 'POST':
        print("post")
        data = json.loads(request.body)
        source_coords = data.get('sourceCoords')
        destination_coords = data.get('destinationCoords')

        print('Source Coordinates:', source_coords)
        print('Destination Coordinates:', destination_coords)
        return render(request, 'api/journey.html')
    return render(request, 'api/journey.html')

def MyProfile(request):
  
  return render(request, 'api/myprofile.html')