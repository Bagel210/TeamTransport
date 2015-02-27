from django.contrib import admin
from app.models import Departures, BusStop, Attraction
# Register your models here.

admin.site.register(Departures)
admin.site.register(BusStop)
admin.site.register(Attraction)
