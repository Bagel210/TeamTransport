from django.shortcuts import render

from app import database

# Create your views here.

#

#database.add_data()

def home(request):
	return render(request,'app/about.html')

def app(request):
	return render(request, 'app/app.html')
