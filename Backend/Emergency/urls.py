from django.conf.urls import url
from . import views

app_name = 'Emergency'

urlpatterns = [
    # Page for Emergency Situation
    # /emergency/
    url(r'^emergency/$', views.emergency, name='emergency'),
]