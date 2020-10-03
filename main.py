#les imports tout propres
import requests
import datetime
import pytz
import os
from dotenv import load_dotenv
load_dotenv()
tempsdeglande = 7200
etatmail = 0
transfert = ""
D = []
bla = []
datetrouvee = False
cours_string = ""
null = "null"

def take_second(elem):
    return elem[:7]

url = os.getenv('url')


def download_calendar():
    r = requests.get(url, allow_redirects=True)
    open('cal.ics', 'wb').write(r.content)


with open('cal.ics', 'r') as my_file:
    for ligne in my_file:
        transfert += ligne
download_calendar
bla = transfert.split("BEGIN:VEVENT")
cours = []
for i in range(len(bla)):
    cours += tuple(bla[i].split("\n"))

for i in range(1, len(bla) - 1):
    cours_string += bla[i].split("\n")[5] + " "

datesdecours = cours_string.split(" DTSTART:")
datesdecours[0] = datesdecours[0][8:]
datesdecours.sort()
ajd = datetime.date.today().strftime("%Y%m%d")
demain_nf = datetime.date.today() + datetime.timedelta(days=1)
demain = demain_nf.strftime("%Y%m%d")

for i in range(0, len(datesdecours)):
    if datesdecours[i][:8] < demain:
        pass
    else:
        if datetrouvee == False:
            print(datesdecours[i])
            datecoursdemain = datesdecours[i]
            datetrouvee = True

        else:
            break
for i in range(0,len(bla)):
    if datecoursdemain in bla[i]:
        numerodecours = i
print(numerodecours)

infocours = str(bla[numerodecours])
print(infocours)
print(infocours[infocours.find("DESCRIPTION;"):infocours.find("\nEND")])


if datecoursdemain == demain :

    coursutc = datetime.datetime.strptime(datecoursdemain, '%Y%m%dT%H%M%SZ')
    target_tz = pytz.timezone('Europe/Paris')
    local_tz = pytz.timezone('UTC')
    courshdp = local_tz.localize(coursutc)
    courshdp = target_tz.normalize(courshdp)

    alarm = (courshdp.hour * 60 + courshdp.minute) * 60 + courshdp.second
    gmailacc = os.getenv('gmailacc')
    gmailsecret = os.getenv('gmailsecret')
    print(alarm-tempsdeglande)
    datas=f"secret={gmailsecret}&to={gmailacc}&device=&priority=normal&payload={alarm-tempsdeglande}"
    print(datas)
    print(requests.post('https://llamalab.com/automate/cloud/message',data=datas,headers={'content-type': 'application/x-www-form-urlencoded'}))
