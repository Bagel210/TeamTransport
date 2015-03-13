from django.db import models
import json


# Create your models here.
class Departures(models.Model):
    valid_from = models.IntegerField()
    day = models.IntegerField(max_length=1)
    #time = models.TimeField()
    service_name = models.CharField(max_length=100)
    destination = models.CharField(max_length=200)

class BusStop(models.Model):
    id = models.IntegerField(primary_key=True)
    stop_name = models.CharField(max_length=200)
    departures = models.CharField(max_length=200)


    def setdepartures(self, x):
        self.departures = json.dumps(x)

    def getdepartures(self, x):
        return json.loads(self.departures)


class Attraction(models.Model):
    bus_stop = models.ForeignKey(BusStop, related_name='closest_stop')
    attraction_name = models.CharField(max_length=100)

class Stops(models.Model):
    stop_id = models.CharField(max_length=20)
    atco_code = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    #locality = models.CharField(max_length=100)
    orientation = models.IntegerField()
    direction = models.CharField(max_length=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    #destinations = models.CharField(max_length=200)
    #services = models.CharField(max_length=200)