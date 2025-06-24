from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse

# Create your views here.

def superuser_check(request):
    User = get_user_model()
    su_list = list(User.objects.filter(is_superuser=True)
                              .values_list('username', flat=True))
    if su_list:
        return HttpResponse('Superusers: ' + ', '.join(su_list))
    else:
        return HttpResponse('No superusers exist')