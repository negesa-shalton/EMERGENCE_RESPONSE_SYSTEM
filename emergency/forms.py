from django.contrib.gis import forms  # Correct import for PointField and OSMWidget
from django import forms as django_forms  # Import standard forms under an alias to avoid confusion
from .models import Incidence

class IncidenceForm(forms.ModelForm):  # Use ModelForm for binding to the model
    class Meta:
        # location = forms.PointField()  # Interactive map widget
        model = Incidence
        fields = '__all__'
       