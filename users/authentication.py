from django.conf import settings
from rest_framework import authentication, exceptions
from . import models
import jwt

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return None
        
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")
        
        user = models.User.objects.filter(email=payload['email']).first()

        return (user, None)