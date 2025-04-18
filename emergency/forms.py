from django.contrib.gis import forms  # Correct import for PointField and OSMWidget
from django import forms as django_forms  # Import standard forms under an alias to avoid confusion
from .models import Incidence

class IncidenceForm(forms.Form):  # Use ModelForm for binding to the model
    location = forms.PointField(widget=forms.OSMWidget(attrs={
        "display_raw": True,
        "geom_type": 'point',
        "map_srid": '4326',
        "template_name": 'report_emergency.html',
        }))  # Interactive map widget
    
    class Meta:
        model = Incidence
        fields = ['name', 'category', 'description', 'severity', 'image', 'location']