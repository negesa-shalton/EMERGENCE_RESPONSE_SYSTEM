from django.contrib import admin

from emergency.models import Health_Facilities, Incidence
from leaflet.admin import LeafletGeoAdmin



# Register your models here.

# class LocationAdmin(LeafletGeoAdmin):
#     list_display = "linked_emergency",

# @admin.register(Incidence)
class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')

class HealthFacilitiesAdmin(LeafletGeoAdmin):
    list_display = ('name','healthcare')

admin.site.register(Incidence,IncidenceAdmin)
admin.site.register(Health_Facilities,HealthFacilitiesAdmin)
