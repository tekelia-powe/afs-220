from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

from pages.models import Users, BookedTrips, SavedTrips

def index(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def mountain (request):

    return render(request, 'pages/mountain.html')

def mountain_tn (request):
    return render(request, 'pages/mountain_tn.html')

def mountain_ca (request):
    return render(request, 'pages/mountain_ca.html')

def register (request):
    return render(request, 'pages/register.html')

def login (request):
    return render(request, 'pages/login.html')

def booked(request):
    if request.method == 'POST':
        #Get form values
        
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        trip_name = request.POST['trip_name']

        # Check if previously booked
        if request.user.is_authenticated:
            user_id = request.user.id
            has_booked = BookedTrips.objects.all().filter(user_id=user_id, trip_name=trip_name)

            if has_booked:
                messages.error(request, 'You have previously requested to book the '+trip_name+ '.')
                return redirect('dashboard')

        booked = BookedTrips(user_email=email, user_phone=phone, user_message=message, user_id= user_id, trip_name=trip_name)
        booked.save()

        messages.success(request, 'You have successfully requested to book the trip.')
        return redirect('/')

def saved(request):
    if request.method == 'POST':
        #Get form values
        
        email = request.POST['email']
        user_id = request.POST['user_id']
        trip_name = request.POST['trip_name']

        # Check if previously booked
        if request.user.is_authenticated:
            user_id = request.user.id
            has_saved = SavedTrips.objects.all().filter(user_id=user_id, trip_name=trip_name)

            if has_saved:
                messages.error(request, 'You have previously saved '+trip_name+ '.')
                return redirect('dashboard')

        saved = SavedTrips(user_email=email,user_id= user_id, trip_name=trip_name)
        saved.save()

        messages.success(request, 'You have successfully saved this trip.')
        return redirect('/')

def dashboard(request):
    booked_trips = BookedTrips.objects.order_by('-trip_name').filter(user_id=request.user.id)
    saved_trips = SavedTrips.objects.order_by('-trip_name').filter(user_id=request.user.id)
    context = {
        'btrips' : booked_trips,
        'strips' : saved_trips,
    }
    return render(request, 'pages/dashboard.html', context)