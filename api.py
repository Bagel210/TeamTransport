# Using Python-Request to poll API
import requests
import json
import pprint as pp

api_code = '0c627af5849e23b0b030bc7352550884'

headers = {"Authorization": "Token " + api_code}

key = "timetables"
stop_number = "36235979"

BASE= "https://tfe-opendata.com/api/v1/"


# @ http://tfe-opendata.readme.io/v1.0/docs/stops
def get_list_of_stops():
    r = requests.get(BASE+'stops')

    if r.status_code == 200:
        return r.json()['stops']


# @ http://tfe-opendata.readme.io/v1.0/docs/services
def get_list_of_services():

    # GET /v1/services
    r = requests.get(BASE+'services')

    if r.status_code == 200:
        return r.json()

    GET /v1/services
    r = requests.get(BASE+'services')

    if r.status_code == 200:
        return r.json()


# @ http://tfe-opendata.readme.io/v1.0/docs/timetables
def get_timetable_for_stop(stop_id):
    r = requests.get(BASE+'timetables/'+stop_id)

    if r.status_code == 200:
        return r.json()

def time_table_between_stops(first_stop, last_stop, date, duration='120'):

    """
    first_stop and last_stop must be on same journey to use this method
    """

    r = requests.get(BASE+'stoptostop-timetable/?start_stop_id=' + first_stop + '&finish_stop_id=' + last_stop + '&date=' + date + '&duration=' + duration)

    if r.status_code == 200:
        return r.json()


def journey_plan(begin_position, end_position, date, time_mode='LeaveAfter'):
    """
    # Positions are tuples of float ->  (e.g. 55.31112,-3.12797)
    # time mode can be either LeaveAfter or ArriveBy
    """

    r = requests.get(BASE + '/directions/?start=' + begin_position + '+&finish=' + end_position + '&date=' + date + '&time_mode=' + time_mode)

    if r.status_code == 200:
        return r.json()

    # Note: must be on same journey
    r = requests.get(BASE+'stoptostop-timetable/?start_stop_id=' + first_stop + '&finish_stop_id=' + last_stop + '&date=' + date + '&duration=' + duration)
    if r.status_code == 200:
        return r.json()




