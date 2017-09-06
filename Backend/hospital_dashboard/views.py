from django.shortcuts import render
from consultancy.models import hospital

# Create your views here.
def hospital_home(request):
    hospital_data=hospital.objects.all()  #TODO specific hospital id match and show only that
    return render(request, 'hospital_dashboard.html', {'hosp_data': hospital_data, })