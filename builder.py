from __future__ import print_function

import datetime
import os.path
import constants

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def parseRawDate(rawDate):
    days = ''
    period = ''
    times = ''
    for char in rawDate:
        if period == '':
            if not char.isalpha():
                days+=char
            else:
                period+=char
        else:
            times+=char
    return (days,period,times)

def validateCredentials():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def buildEvents(eventList,creds):
    try:
        service = build('calendar', 'v3', credentials=creds)
        
        for rawEvent in eventList:
            print(rawEvent)
            try:
                event = {
                'summary': 'Google I/O 2015',
                'location': '800 Howard St., San Francisco, CA 94103',
                'description': 'A chance to hear more about Google\'s developer products.',
                'start': {
                    'dateTime': '2015-05-28T09:00:00-07:00',
                    'timeZone': constants.TIMEZONE,
                },
                'end': {
                    'dateTime': '2015-05-28T17:00:00-07:00',
                    'timeZone': constants.TIMEZONE,
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

                event = service.events().insert(calendarId='primary', body=event).execute()
                print('Event created: %s' % (event.get('htmlLink')))
            
            except HttpError as error:
                print(f'An error occured: {error}')



    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()