from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.utils.dateformat import format
import datetime

from app.models import BusStop, Attraction, Departures

from app import database
from app import api

# Create your views here.

#

#database.add_data()

def journeyPlan(request):
    context = RequestContext(request)

    attractions_list = Attraction.objects.all() #.order_by('attraction_name')
    busStop_list = BusStop.objects.all() #.order_by('id')

    return render_to_response(
        'app/app.html',
        {'attractions_list': attractions_list,
         'busStop_list': busStop_list}, context)

def route(request):
    context = RequestContext(request)
    route = api.journey_plan("55.90064,-3.39297", "55.8765,-3.337341", format(datetime.datetime.now(), u'U'))['journeys'][0]['legs']

    return render_to_response(
        'app/route.html',
        {'route': route}, context)

def home(request):
    return render(request,'app/about.html')

#def app(request):
#    return render(request, 'app/app.html')
