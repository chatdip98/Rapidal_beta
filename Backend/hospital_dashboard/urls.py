from django.conf.urls import url
from . import views

app_name = 'hospital_dashboard'

urlpatterns = [

    # This is the Respective Home Pages of The Hospitals
    # /hospital_home/
    url(r'^hospital_home/$', views.hospital_home, name='hospital_home'),

]