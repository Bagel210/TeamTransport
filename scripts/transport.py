# Using Python-Request to poll API
import requests
import pprint as pp

api_code = '0c627af5849e23b0b030bc7352550884'

headers = {"Authorization" : "Token "+ api_code}

key ="timetables"
stop_number = "36235979"


r = requests.get('https://tfe-opendata.com/api/v1/'+key+'/'+stop_number, headers=headers)
# r = requests.get('https://tfe-opendata.com/api/v1/timetables/36235979', headers=headers)

if r.status_code == 200:
	pp.pprint(r.json())
else:
	print r.status_code

# {u'departures': [{u'day': 0,
#                   u'destination': u'Ocean Terminal',
#                   u'note_id': None,
#                   u'service_name': u'N22',
#                   u'time': u'0:18',
#                   u'valid_from': 1414886400},
#                   .
#                   .
#                   .
#  u'stop_id': 36235979,
#  u'stop_name': u'Elm Row'}