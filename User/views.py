from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Here you would typically save the user to the database
        # For example:
        # user = User.objects.create_user(username=username, password=password, email=email)
        
        return HttpResponse("User registered successfully.")
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Login successful.")
        else:
            return HttpResponse("Invalid credentials.")
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return HttpResponse("Logged out successfully.")
