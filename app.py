from getpass import getuser
from webbrowser import get
from login import getUserData
from scraper import getCourses

user = getUserData()

process = getCourses(user)

print(process)
