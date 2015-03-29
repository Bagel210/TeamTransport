from django.contrib import admin
from app.models import Departures, BusStop, Attraction, Stops, UserProfile
# Register your models here.

admin.site.register(Departures)
admin.site.register(BusStop)
admin.site.register(Attraction)
admin.site.register(Stops)
admin.site.register(UserProfile)