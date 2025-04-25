import os
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource

from emergency.models import Health_Facilities

health_facilities_mapping = {
    'name': 'name',
    'amenity': 'amenity',
    'healthcare': 'healthcare',
    'geom': 'MULTIPOINT',
}

def load_data(verbose=True):
    file = os.getcwd() + "/data/health_facilities_2.gpkg"
    data_source = DataSource(file)
    facilities_layer = data_source[0].name

    facilities_layer_mapping = LayerMapping(
        Health_Facilities,file,health_facilities_mapping,layer=facilities_layer
    )
    facilities_layer_mapping.save(strict=True,verbose=verbose)
