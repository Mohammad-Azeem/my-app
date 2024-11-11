"""
Create a single view that collects the necessary data from the database schemas
"""

from django.shortcuts import render
from .models import User  # import user model from models
from .models import AppUsage
from .models import Transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def my_authenticated_view(request):
    # Your view logic here


def my_authenticated_view(request):
    username = request.user.username
    # Your view logic here


def user_data_view(request):
    users = User.objects.all()  # Retrieve all user data from the database
    return render(request, 'user_data.html', {'users': users})  
    # pass the retrieved data to a template for rendering. 
    # create a corresponding HTML template (user_data.html) to display the data inside template directory.


def app_usage_data_view(request):
    appUsages = AppUsage.objects.all()  # Retrieve all user data from the database
    return render(request, 'app_usage_data.html', {'appUsages': appUsages})


def transaction_data_view(request):
    transactions = Transaction.objects.all()  # Retrieve all user data from the database
    return render(request, 'transaction_data.html', {'transactions': transactions})

class UserAuthenticationView(APIView):
    def post(self, request, format=None):
        serializer = UserAuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
