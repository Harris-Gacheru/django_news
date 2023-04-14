from . import models, serializer as user_serializer, authentication
from rest_framework import views, response, status, permissions
import jwt
import datetime
from django.conf import settings

class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        if serializer.is_valid():
            user_serializer.UserSerializer().create(serializer.validated_data) #save user data & set password

            return response.Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPI(views.APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        #check if user exists
        user = models.User.objects.filter(email=email).first()

        if user is None:
            return response.Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not user.check_password(raw_password=password):
            return response.Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        payload = dict(
            id = user.id,
            email = user.email,
            exp = datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            iat = datetime.datetime.utcnow()
        )

        token = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')

        resp = response.Response()

        resp.set_cookie(key='jwt', value=token, httponly=True)
        resp.data = {'message': 'Logged in successfully'}

        return resp
    
class LogoutAPI(views.APIView):
    authentication_classes = (authentication.CustomAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie('jwt')
        resp.data = {'message': 'Logged out'}

        return resp

class UserAPI(views.APIView):
    authentication_classes = (authentication.CustomAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        serializer = user_serializer.UserSerializer(request.user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
