from django.conf.urls import url
from . import views

app_name = 'consultancy'

urlpatterns = [
    # The Home page of Non-Emergency Situations
    # /consulting/
    url(r'^consulting/$', views.all_consulted, name='all_consulted'),

]