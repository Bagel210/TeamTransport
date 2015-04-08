from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse


from django.utils.dateformat import format
import datetime
import json

from app.forms import UserForm, UserProfileForm
from app.models import BusStop, Attraction, Departures, Stops, UserProfile

from app import database
from app import api

# Create your views here.

#

# database.add_data()
# database.add_stops()
# database.add_attractions()

def journeyPlan(request):
    context = RequestContext(request)

    attractions_list = Attraction.objects.all() # .order_by('attraction_name')
    # busStop_list = BusStop.objects.all() #.order_by('id')

    stop_list = Stops.objects.all().order_by('name')

    return render_to_response(
        'app/app.html',
        {'attractions_list': attractions_list,
         'stop_list': stop_list}, context)

def route(request):

    print(request.GET.get("stop1id", "default_value"))
    print(request.GET.get("stop2id", "default_value"))
    print(request.method)
    print(request.POST.dict())
    print(request.GET.dict())
    print(request.body)

    stop1_id = request.POST.dict()['stop1id']
    stop2_id = request.POST.dict()['stop2id']

    stop1 = Stops.objects.get(stop_id=stop1_id)
    stop2 = Stops.objects.get(stop_id=stop2_id)

    location1 = stop1.latitude, stop1.longitude
    location2 = stop2.latitude, stop2.longitude

    print(location1, location2)

    context = RequestContext(request)
    # route = api.journey_plan(location1[0] + "," + location1[1], location2[0] + "," + location2[1], format(datetime.datetime.now(), u'U'),
    #                          "LeaveAfter")
    route = {'request_time': 1427669687, 'journeys': [{'duration': 106, 'legs': [{'duration': 12, 'start': {'name': 'Start', 'latitude': 55.900642, 'time': 1427684640, 'longitude': -3.392967}, 'finish': {'name': 'Wilkieston, at Post Office on Main Street', 'latitude': 55.901193, 'stop_name': None, 'longitude': -3.40695, 'stop_id': 0, 'time': 1427685360}, 'mode': 'walk'}, {'duration': 13, 'service': {'name': '109', 'waypoints': [], 'destination': 'Edinburgh Longstone'}, 'start': {'name': 'Wilkieston, at Post Office on Main Street', 'latitude': 55.901193, 'stop_name': None, 'longitude': -3.40695, 'stop_id': 0, 'time': 1427685360}, 'finish': {'name': 'Longstone, after Longstone Terrace on Longstone Road', 'latitude': 55.925714, 'stop_name': 'Calder Road', 'longitude': -3.268856, 'stop_id': 36236752, 'time': 1427686140}, 'mode': 'bus'}, {'duration': 4, 'start': {'name': 'Longstone, after Longstone Terrace on Longstone Road', 'latitude': 55.925714, 'stop_name': 'Calder Road', 'longitude': -3.268856, 'stop_id': 36236752, 'time': 1427686140}, 'finish': {'name': 'Longstone, at Longstone Cottages on Longstone Road', 'latitude': 55.925205, 'stop_name': 'Longstone Cottages', 'longitude': -3.263334, 'stop_id': 36235365, 'time': 1427686380}, 'mode': 'walk'}, {'duration': 17, 'service': {'name': '44A', 'waypoints': [[{'stop_id': 36235365, 'latitude': 55.9251, 'longitude': -3.26341}], [{'latitude': 55.925, 'longitude': -3.26208}], [{'stop_id': 36235364, 'latitude': 55.9255, 'longitude': -3.25899}], [{'latitude': 55.9251, 'longitude': -3.25562}], [{'latitude': 55.9247, 'longitude': -3.25416}], [{'stop_id': 36235362, 'latitude': 55.924, 'longitude': -3.25223}], [{'latitude': 55.9233, 'longitude': -3.25073}], [{'latitude': 55.9226, 'longitude': -3.24957}], [{'stop_id': 36236296, 'latitude': 55.9222, 'longitude': -3.25023}], [{'latitude': 55.9221, 'longitude': -3.25112}], [{'latitude': 55.9213, 'longitude': -3.25292}], [{'stop_id': 36235368, 'latitude': 55.9208, 'longitude': -3.25453}], [{'latitude': 55.9205, 'longitude': -3.2555}], [{'stop_id': 36235369, 'latitude': 55.9187, 'longitude': -3.25832}], [{'latitude': 55.9183, 'longitude': -3.259}], [{'latitude': 55.9179, 'longitude': -3.25942}], [{'stop_id': 36235372, 'latitude': 55.9163, 'longitude': -3.25994}], [{'stop_id': 36235373, 'latitude': 55.915, 'longitude': -3.26103}], [{'latitude': 55.9141, 'longitude': -3.26172}], [{'stop_id': 36235374, 'latitude': 55.9131, 'longitude': -3.26294}], [{'stop_id': 36235375, 'latitude': 55.9119, 'longitude': -3.26511}], [{'latitude': 55.9105, 'longitude': -3.26796}], [{'stop_id': 36235376, 'latitude': 55.9099, 'longitude': -3.26855}], [{'latitude': 55.9089, 'longitude': -3.26965}], [{'stop_id': 36235378, 'latitude': 55.9084, 'longitude': -3.27066}], [{'stop_id': 36237486, 'latitude': 55.9075, 'longitude': -3.27372}], [{'latitude': 55.9067, 'longitude': -3.27633}], [{'stop_id': 36237492, 'latitude': 55.906, 'longitude': -3.27837}], [{'latitude': 55.9055, 'longitude': -3.27946}], [{'stop_id': 36237494, 'latitude': 55.9048, 'longitude': -3.28159}], [{'stop_id': 36237495, 'latitude': 55.904, 'longitude': -3.28374}], [{'stop_id': 36237496, 'latitude': 55.9033, 'longitude': -3.28517}], [{'latitude': 55.9027, 'longitude': -3.28669}], [{'stop_id': 36237524, 'latitude': 55.9017, 'longitude': -3.28944}], [{'latitude': 55.9014, 'longitude': -3.29037}], [{'stop_id': 36237527, 'latitude': 55.9004, 'longitude': -3.29432}], [{'stop_id': 36237528, 'latitude': 55.8991, 'longitude': -3.2986}], [{'latitude': 55.8986, 'longitude': -3.30058}], [{'stop_id': 36237532, 'latitude': 55.8974, 'longitude': -3.30305}], [{'latitude': 55.8972, 'longitude': -3.30364}], [{'latitude': 55.897, 'longitude': -3.3051}], [{'stop_id': 36237563, 'latitude': 55.8968, 'longitude': -3.30604}], [{'latitude': 55.8964, 'longitude': -3.30751}], [{'latitude': 55.8963, 'longitude': -3.30912}], [{'stop_id': 36242659, 'latitude': 55.8961, 'longitude': -3.31003}], [{'stop_id': 36237539, 'latitude': 55.895, 'longitude': -3.31319}], [{'latitude': 55.8936, 'longitude': -3.31692}], [{'stop_id': 36237543, 'latitude': 55.8934, 'longitude': -3.31788}], [{'latitude': 55.893, 'longitude': -3.32008}], [{'stop_id': 36237549, 'latitude': 55.8927, 'longitude': -3.32082}], [{'latitude': 55.8921, 'longitude': -3.32205}], [{'latitude': 55.8919, 'longitude': -3.32301}], [{'stop_id': 36237547, 'latitude': 55.8916, 'longitude': -3.32405}], [{'stop_id': 36237545, 'latitude': 55.8901, 'longitude': -3.32969}], [{'latitude': 55.8891, 'longitude': -3.33325}], [{'latitude': 55.889, 'longitude': -3.33462}], [{'latitude': 55.889, 'longitude': -3.33606}], [{'latitude': 55.8886, 'longitude': -3.33776}], [{'latitude': 55.8886, 'longitude': -3.33809}], [{'stop_id': 36234942, 'latitude': 55.8882, 'longitude': -3.33841}], [{'latitude': 55.8875, 'longitude': -3.339}]], 'destination': 'Balerno'}, 'start': {'name': 'Longstone, at Longstone Cottages on Longstone Road', 'latitude': 55.925205, 'stop_name': 'Longstone Cottages', 'longitude': -3.263334, 'stop_id': 36235365, 'time': 1427688300}, 'finish': {'name': 'Balerno, at Balerno High School on Bridge Road', 'latitude': 55.886588, 'stop_name': 'Balerno High', 'longitude': -3.339542, 'stop_id': 36234943, 'time': 1427689320}, 'mode': 'bus'}, {'duration': 4, 'service': {'name': '44', 'waypoints': [[{'stop_id': 36234943, 'latitude': 55.887, 'longitude': -3.33919}], [{'latitude': 55.8856, 'longitude': -3.33999}], [{'stop_id': 36234957, 'latitude': 55.8856, 'longitude': -3.33933}], [{'latitude': 55.8856, 'longitude': -3.33857}], [{'latitude': 55.8854, 'longitude': -3.33794}], [{'latitude': 55.8851, 'longitude': -3.3376}], [{'stop_id': 36234958, 'latitude': 55.8843, 'longitude': -3.33745}], [{'latitude': 55.8838, 'longitude': -3.33745}], [{'latitude': 55.8836, 'longitude': -3.33774}], [{'latitude': 55.8833, 'longitude': -3.33826}], [{'latitude': 55.8831, 'longitude': -3.33862}], [{'stop_id': 36234962, 'latitude': 55.8828, 'longitude': -3.33885}], [{'latitude': 55.8813, 'longitude': -3.33934}], [{'latitude': 55.8807, 'longitude': -3.33939}], [{'stop_id': 36234953, 'latitude': 55.8788, 'longitude': -3.3382}], [{'latitude': 55.8766, 'longitude': -3.33666}]], 'destination': 'Wallyford or Whitecraig'}, 'start': {'name': 'Balerno, at Balerno High School on Bridge Road', 'latitude': 55.886588, 'stop_name': 'Balerno High', 'longitude': -3.339542, 'stop_id': 36234943, 'time': 1427690760}, 'finish': {'name': 'Balerno, at Lothian Buses Terminus on Cockburn Crescent', 'latitude': 55.876582, 'stop_name': 'Mansfield Road', 'longitude': -3.337455, 'stop_id': 36234964, 'time': 1427691000}, 'mode': 'bus'}, {'duration': 0, 'start': {'name': 'Balerno, at Lothian Buses Terminus on Cockburn Crescent', 'latitude': 55.876582, 'stop_name': 'Mansfield Road', 'longitude': -3.337455, 'stop_id': 36234964, 'time': 1427691000}, 'finish': {'name': 'Destination', 'latitude': 55.876503, 'time': 1427691000, 'longitude': -3.337341}, 'mode': 'walk'}]}], 'request_id': 1427669692165}

    return render_to_response(
        'app/route.html',
        {'route': route['journeys'][0]['legs']}, context)


def home(request):
    return render(request, 'app/about.html')

def register(request):

    context = RequestContext(request)
    registered = False
    print(request.method)

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
        'app/authentication/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/Home/')
            else:
                return HttpResponse("Your SeeEdin account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Faulty credentials.")

    else:
        return render_to_response('app/authentication/login.html', {}, context)


def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/Home/')
