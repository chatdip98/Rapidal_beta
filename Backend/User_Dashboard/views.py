from django.shortcuts import render, get_object_or_404
from .models import user,ecnomic_condition


def show_user(request ):
    all_users=user.objects.all()
    return render(request, 'show_user.html',{'all_users_data' : all_users,})
