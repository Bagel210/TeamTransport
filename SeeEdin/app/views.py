from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from app.models import BusStop, Attraction, Departures

from app import database

# Create your views here.

#

#database.add_data()
#database.data_from_api()

def journeyPlan(request):
    context = RequestContext(request)

    attractions_list = Attraction.objects.all() #.order_by('attraction_name')
    busStop_list = BusStop.objects.all() #.order_by('id')

    return render_to_response(
        'app/app.html',
        {'attractions_list': attractions_list,
         'busStop_list': busStop_list}, context)

def home(request):
    return render(request,'app/about.html')

#def app(request):
#    return render(request, 'app/app.html')
