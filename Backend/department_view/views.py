from django.shortcuts import render
from consultancy.models import hospital, department

# Create your views here.
def show_dept_details(request):
    all_hospitals = hospital.objects.all()       #TODO Department ID mtch and respective giving
    return render(request, 'show_dept.html', {'all_hosps': all_hospitals, })