from getpass import getuser
from webbrowser import get
from login import getUserData
from scraper import getCourses
from builder import validateCredentials, buildEvents
import datetime

#Fetch user data from server
user = getUserData()
process = getCourses(user)

#Transform fetched data into Google Calendar API event format.
print(process)

events = []

for k in process.keys():
    event = {
        'summary': k,
        'location': process[k][0],
        'start':{

        },
        'end':{

        },
        'recurrence': [
        'RRULE:FREQ=WEEKLY;COUNT=10'
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    print(type(process[k]))
    print(event)

#Validate Google Calendar API credentials and build events

# event = {
#                 'summary': 'Google I/O 2015',
#                 'location': '800 Howard St., San Francisco, CA 94103',
#                 'start': {
#                     'dateTime': '2015-05-28T09:00:00-07:00',
#                     'timeZone': constants.TIMEZONE,
#                 },
#                 'end': {
#                     'dateTime': '2015-05-28T17:00:00-07:00',
#                     'timeZone': constants.TIMEZONE,
#                 },
#                 'recurrence': [
#                     'RRULE:FREQ=WEEKLY;COUNT=10'
#                 ],
#                 'reminders': {
#                     'useDefault': False,
#                     'overrides': [
#                     {'method': 'email', 'minutes': 24 * 60},
#                     {'method': 'popup', 'minutes': 10},
#                     ],
#                 },
#                 }




#buildEvents(events,validateCredentials())
