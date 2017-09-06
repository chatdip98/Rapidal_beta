from django.conf.urls import url
from . import views

app_name = 'User_Dashboard'

urlpatterns = [

    # Home page for Users
    # /user/   #TODO user ID matching and showing
    url(r'^user/$', views.show_user, name='show_user'),
]