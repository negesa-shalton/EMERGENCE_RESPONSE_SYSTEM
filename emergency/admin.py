from django.contrib import admin

from emergency.models import Health_Facilities, Incidence, Location
from leaflet.admin import LeafletGeoAdmin



# Register your models here.

# class LocationAdmin(LeafletGeoAdmin):
#     list_display = "linked_emergency",

# @admin.register(Incidence)
class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('category','area_name','severity','description','reported_by')

class HealthFacilitiesAdmin(LeafletGeoAdmin):
    list_display = ('name','healthcare')

class LocationAdmin(LeafletGeoAdmin):
    list_display = ('user','latitude','longitude')


admin.site.register(Incidence,IncidenceAdmin)
admin.site.register(Health_Facilities,HealthFacilitiesAdmin)
admin.site.register(Location)
