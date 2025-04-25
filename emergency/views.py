from django.shortcuts import render
from rest_framework import viewsets
from emergency.forms import IncidenceForm
from emergency.models import Incidence,Health_Facilities, Location
from .serializers import Health_FacilitiesSerializer
from django.http import JsonResponse
from geopy.distance import geodesic
import json

def index(request):
    return render(request,'index.html')

# Report Emergency View
def report_emergency(request):
    form = IncidenceForm()
    print(IncidenceForm)
    # if request.method == 'GET':
    #     form = IncidenceForm(request.POST)
    #     # print(IncidenceForm)
    #     # if form.is_valid():
    #     #     incidence = Incidence(
    #     #     name=form.cleaned_data['name'],
    #     #     category=form.cleaned_data['category'],
    #     #     description=form.cleaned_data['description'],
    #     #     severity=form.cleaned_data['severity'],
    #     #     image=form.cleaned_data['image'],
    #     #     location=form.cleaned_data['location']
    #     #     )
    #     #     incidence.reported_by = request.user  # Ensure this works only if the user is logged in
    #     #     incidence.save()
    #     #     # Redirect to emergency list view, not a template path directly
    #     #     # return redirect('emergency_list')  
    # else:
    #     form = IncidenceForm()  # Initialize form if the request is GET or invalid POST
    return render(request, 'report_emergency.html', {'form': form})  # Proper context for the template

# Emergency List View
def emergency_list(request):
    emergencies = Incidence.objects.all()  # Use `.all()` to fetch all records from the model
    return render(request, 'emergency_list.html', {'emergencies': emergencies})  # Correct context variable name

########Viewset for API
class Health_FacilitiesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Health_Facilities.objects.values()
    serializer_class = Health_FacilitiesSerializer

def closest_health_facility(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    user_location = latitude,longitude
    Health_Facilities_Distance = {}
    for facility in Health_Facilities.objects.all()[:100]:
        facility_location = facility.latitude, facility.longitude

        #Calculate the distance between the user and the station
        distance = (user_location,facility_location).km
        Health_Facilities_Distance[distance] = facility_location

    min_facility_distance = min(Health_Facilities_Distance)
    facility_coordinates = Health_Facilities_Distance[min_facility_distance]

    return JsonResponse({
        'coordinates': facility_coordinates,
        'distance': min_facility_distance
    })

def save_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            #Extract location details
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            #Validate the data
            if not all([latitude,longitude]):
                return JsonResponse({
                    'status': 'error',
                    'message': 'Incomplete Location data'
                },status=400)
            
            #Save user location
            Location.objects.update_or_create(
                user = request.user,
                defaults = {
                    'latitude': latitude,
                    'longitude':longitude
                }
            )
            return JsonResponse({
                'status':'success',
                'message':'Location Saved Successfully'
            })

        except Exception as e:
            return JsonResponse({
            'status': 'error',
                'message': str(e)
            },status=500)
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    },status=400)

