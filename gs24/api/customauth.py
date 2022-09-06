#This file helps us to identify Anauthenticated Users
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username=request.GET.get('username') #This username is given by clint
        # username=request.POST.get('username') #I have to learn about //SESSION//
        if username is None:
            return None
        try:
            user=User.objects.get(username=username) #This username is already exist in Django's Admin page
        except User.DoesNotExist:
            raise AuthenticationFailed('No such  bhai!!')
        return (user, None) #If the user exist can perform operations otherwise //No such  bhai!!//