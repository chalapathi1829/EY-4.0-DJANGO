from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Myapp")
def home(request):
    return HttpResponse("my home page")
def dashboard(request):
    return render(request,'myapp/index.html')
def login(request):
    return render(request,'myapp/login.html')
def registration(request):
    return render(request,'myapp/registration.html')
def movie(request):
    return render(request,'myapp/movie.html')
def home(request):
    return render(request,'myapp/home.html')
def about(request):
    return render(request,'myapp/about.html')
def contact(request):
    return render(request,'myapp/contact.html')