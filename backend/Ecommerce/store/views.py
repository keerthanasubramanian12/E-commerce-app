from django.shortcuts import render, redirect
from .models import Userprofile
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'index.html')

class SignupView(APIView):
    
    # Create a new user
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        phone_number = request.data.get('phone_number')
        confirm_password = request.data.get('confirm_password')
        linkedin = request.data.get('linkedin')
        
        if password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=400)

        if Userprofile.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=400)

        user = Userprofile(name=name, email=email, password=password, phone_number=phone_number, linkedin=linkedin)
        user.save()

        return Response({'message': 'User created successfully'}, status=201)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = Userprofile.objects.filter(email=email, password=password).first()
        
        if user:
            return Response({'message': 'Login successful'}, status=200)
        else:
            return Response({'error': 'Invalid email or password'}, status=401)
    