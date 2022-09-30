import datetime
from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'client important.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


pprint(dir(service))

request_body = {
    'summary': 'python'
}

# to create event

responses = service.calendars().insert(body=request_body).execute()
print(responses)

# to delete event

# response = service.calendars().delete(calendarId='3p3v1tn5e5a2d7lncihdk76bao@group.calendar.google.com').execute()
# print(response)

# list
# response = service.calendarList().list().execute()
# pprint(response)


# create event
'''
event = {
    'summary': 'Python',
    'location': '800 Howard St., San Francisco, CA 94103',
    'description': 'A chance to hear more about Google\'s developer products.',
    'start': {
        'dateTime': '2022-08-30T09:00:00-07:00',

        

    },
    'end': {
        'dateTime': '2022-08-30T17:00:00-07:00',

    }
}
response = service.events().insert(calendarId='primary', body=event).execute()
pprint(response)
'''
# delete the event

#response = service.events().delete(calendarId='primary', eventId='27hq6uvlbna44vjmcp3nqc930s').execute()

#get the event


# response = service.events().get(calendarId='primary', eventId='3krpsdgucjqr76u6ur1n0fs66c').execute()

# quickadd
'''
created_event = service.events().quickAdd(
    calendarId='primary',
    text='Appointment at Somewhere on September 2nd 2022 10am-10:25am').execute()

print(created_event['id'])'''