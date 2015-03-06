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
	# Note: must be on same journey
	r = requests.get(BASE+'stoptostop-timetable/?start_stop_id='+first_stop+'&finish_stop_id='+last_stop+'&date='+date+'&duration='+duration)

	if r.status_code == 200:
		return r.json()




