from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse


from django.utils.dateformat import format
import datetime

from app.forms import UserForm, UserProfileForm
from app.models import BusStop, Attraction, Departures, Stops, UserProfile

from app import database
from app import api

# Create your views here.

#

#database.add_data()
#database.add_stops()

def journeyPlan(request):
    context = RequestContext(request)

    attractions_list = Attraction.objects.all() #.order_by('attraction_name')
    busStop_list = BusStop.objects.all() #.order_by('id')

    stop_list = Stops.objects.all().order_by('name')

    return render_to_response(
        'app/app.html',
        {'attractions_list': attractions_list,
         'busStop_list': busStop_list,
         'stop_list': stop_list}, context)

def route(request):
    context = RequestContext(request)
    route = api.journey_plan("55.90064,-3.39297", "55.8765,-3.337341", format(datetime.datetime.now(), u'U'),
                             "LeaveAfter")
    print(route)

    return render_to_response(
        'app/route.html',
        {'route': route}, context)

def home(request):
    return render(request,'app/about.html')

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
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
                return HttpResponse("Your AllExplore account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Faulty credentials.")

    else:
        return render_to_response('app/authentication/login.html', {}, context)


def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/Home/')
