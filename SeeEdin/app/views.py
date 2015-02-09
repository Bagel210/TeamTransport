from django.shortcuts import render

# Create your views here.

#
def home(request):
	return render(request,'app/about.html')

def app(request):
	return render(request, 'app/app.html')
