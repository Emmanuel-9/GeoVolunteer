from django.shortcuts import render
from .models import Event, Volunteer, Location, Admin, Organization

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteer_list.html', {'volunteers': volunteers})

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location_list.html', {'locations': locations})

def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'admin_list.html', {'admins': admins})

def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_list.html', {'organizations': organizations})


# Create your views here.
