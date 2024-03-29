from app import transport, api
from app.models import Departures, BusStop, Attraction, Stops

data = transport.call_api()
list_of_stops = api.get_list_of_stops()
list_of_services = api.get_list_of_services()


def add_data():

    departure_values = data['departures']
    list_of_departures = []
    for departure_value in departure_values:
        departure = Departures.objects.create(
            valid_from=departure_value['valid_from'],
            day=departure_value['day'],
            #time=departure_value['time'],
            service_name=departure_value['service_name'],
            destination=departure_value['destination']
        )
        list_of_departures.append(departure)

    busStop = BusStop.objects.create(
        id=data['stop_id'],
        stop_name=data['stop_name'],
        departures=list_of_departures
    )

def add_stops():

    stop_values = list_of_stops['stops']
    stop_object_list = []
    for stop_value in stop_values:
        stop = Stops.objects.create(
            stop_id=stop_value['stop_id'],
            atco_code=stop_value['atco_code'],
            name=stop_value['name'],
            #locality=stop_value['locality'],
            orientation=stop_value['orientation'],
            direction=stop_value['direction'],
            latitude=stop_value['latitude'],
            longitude=stop_value['longitude'],
            #destinations=stop_value['destinations'],
            #services=stop_value['services']
        )
        stop_object_list.append(stop)

    #services_values = list_of_services['services']


def add_attractions():

    stops = Stops.objects.all()
    for stop in stops:
        if stop.stop_id == "36242342":
            attraction1 = Attraction.objects.create(
                bus_stop=stop,
                attraction_name="Edinburgh Castle"
            )
        if stop.stop_id == "36235925":
            attraction2 = Attraction.objects.create(
                bus_stop=stop,
                attraction_name="Edinburgh Zoo"
            )
        if stop.stop_id == "36235879":
            attraction3 = Attraction.objects.create(
                bus_stop=stop,
                attraction_name="North Bridge"
            )