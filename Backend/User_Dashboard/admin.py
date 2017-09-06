from django.contrib import admin
from consultancy.models import state, city, hospital_price_slab, hospital, department, doctors
from User_Dashboard.models import ecnomic_condition, user

# Register your models here.

admin.site.register(user)
admin.site.register(ecnomic_condition)
admin.site.register(state)
admin.site.register(city)
admin.site.register(hospital)
admin.site.register(hospital_price_slab)
admin.site.register(department)
admin.site.register(doctors)