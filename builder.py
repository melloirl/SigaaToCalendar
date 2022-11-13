import datetime
import os.path
import constants

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events.owned']

class rawDateParser():
    def __init__(self,rawDate):
        self.days = ''
        self.period = ''
        self.times = ''
        for char in rawDate:
            if self.period == '':
                if not char.isalpha():
                    self.days+=char
                else:
                    self.period+=char
            else:
                self.times+=char

    def getDays(self):
        parsedDays = []
        for char in self.days:
            match char:
                case '2':
                    parsedDays.append('MO')
                case '3':
                    parsedDays.append('TU')
                case '4':
                    parsedDays.append('WE')
                case '5':
                    parsedDays.append('TH')
                case '6':
                    parsedDays.append('FR')
                case '7':
                    parsedDays.append('SA')
        
        return ','.join(parsedDays)
    
    def getHour(self):
        match self.period:
            case 'M':
                match self.times[0]:
                    case '1':
                        return 8
                    case '3':
                        return 10
                    case '5':
                        return 12
            case 'T':
                match self.times[0]:
                    case '2':
                        return 14
                    case '4':
                        return 16
                    case '6':
                        return 18
            case 'N':
                match self.times[0]:
                    case '1':
                        return 19
                    case '3':
                        return 20

    def getEventStart(self):
        def nextWeekday(d, weekday, hour):
            daysAhead = weekday - d.weekday()
            hoursAhead = hour - d.hour
            minuteAhead = 0 - d.minute
            secondAhead = 0 - d.second
            msAhead = 0 - d.microsecond
            if daysAhead <= 0: # Target day already happened this week
                daysAhead += 7
            if hoursAhead <= 0: # Target day already happened this week
                hoursAhead += 24
            if minuteAhead <= 0:
                minuteAhead +=59
            if secondAhead <= 0:
                secondAhead +=60
            if msAhead <= 0:
                msAhead+=0

            return d + datetime.timedelta(days=daysAhead,hours=hoursAhead,minutes=minuteAhead,seconds=secondAhead,microseconds=msAhead)

        d = datetime.datetime.now()
        startDay = nextWeekday(d, int(self.days[0])-2,self.getHour()-1) # 0 = Monday, 1=Tuesday, 2=Wednesday...
        return startDay
    
    def getEventEnd(self):
        return self.getEventStart() + datetime.timedelta(hours=1,minutes=55)


def validateCredentials(): #Standalone application approach. On web view, this won't be saved whatsoever.
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
    print('Builder starting...')
    try:
        service = build('calendar', 'v3', credentials=creds)
        for event in eventList:
            print(f"Event being added: {event['summary']}.")
            print(f"    ---> starting from: {event['start']['dateTime']} ")
            print(f"    ---> every: {event['recurrence']}")
            try:
                insertedEvent = service.events().insert(calendarId='primary', body=event).execute()
                print('Event created: %s' % (insertedEvent.get('htmlLink')))
            
            except HttpError as error:
                print(f'An error occured: {error}')



    except HttpError as error:
        print('An error occurred: %s' % error)
    
    print('Building finished.')