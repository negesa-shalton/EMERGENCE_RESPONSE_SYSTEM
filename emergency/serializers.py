from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Health_Facilities

class Health_FacilitiesSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Health_Facilities
        geo_field = "geom"
        fields = "__all__"