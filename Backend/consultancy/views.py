from django.shortcuts import render, get_object_or_404
from .models import hospital, hospital_price_slab


def all_consulted(request ):
    all_hospitals=hospital.objects.all()
    return render(request, 'consult_hos.html',{'all_hosps' : all_hospitals,})

'''    
def details_alumni(request, username_roll_request):
    alumni_var = get_object_or_404(Alumni, user_name=username_roll_request)

    return render(request, 'alumni_profile.html', {'alumni': alumni_var})   
'''