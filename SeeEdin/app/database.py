from app import transport
from app.models import Departures, BusStop, Attraction

data = transport.call_api()

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

    attractionOne = Attraction.objects.create(
        bus_stop=busStop,
        attraction_name='An Attraction at Elm Row'
    )