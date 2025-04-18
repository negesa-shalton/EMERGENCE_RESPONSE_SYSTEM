from django.shortcuts import render, redirect
from emergency.forms import IncidenceForm
from emergency.models import Incidence

# Report Emergency View
def report_emergency(request):
    if request.method == 'POST':
        form = IncidenceForm(request.POST)
        if form.is_valid():
            incidence = form.save()
            incidence.reported_by = request.user  # Ensure this works only if the user is logged in
            incidence.save()
            # Redirect to emergency list view, not a template path directly
            # return redirect('emergency_list')  
    else:
        form = IncidenceForm()  # Initialize form if the request is GET or invalid POST
    return render(request, 'report_emergency.html', {'form': form})  # Proper context for the template

# Emergency List View
def emergency_list(request):
    emergencies = Incidence.objects.all()  # Use `.all()` to fetch all records from the model
    return render(request, 'emergency_list.html', {'emergencies': emergencies})  # Correct context variable name