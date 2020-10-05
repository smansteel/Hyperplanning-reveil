#les imports tout propres
import requests
import datetime
import pytz
import os
import utilisateur0
transfert = ""
D = [""]
bla = []
datetrouvee = False
cours_string = ""
ajd = datetime.date.today().strftime("%Y%m%d")
demain_nf = datetime.date.today() + datetime.timedelta(days=1)
demain = demain_nf.strftime("%Y%m%d")
cours = []
dossier = os.listdir()

def take_second(elem):
    return elem[:7]

url = utilisateur0.url_calendrier
tempsdeglande = int(utilisateur0.temps_a_reveiller_avant_les_cours)

def download_calendar():
    r = requests.get(url, allow_redirects=True)
    open('cal.ics', 'wb').write(r.content)
    print("cal updated")

download_calendar()
with open('cal.ics', 'r') as my_file: #hopla gros bourrin on met tout dans un string
    for ligne in my_file:
        transfert += ligne

bla = transfert.split("BEGIN:VEVENT")

for i in range(len(bla)):
    cours += tuple(bla[i].split("\n"))

for i in range(1, len(bla) - 1):
    cours_string += bla[i].split("\n")[5] + " "

datesdecours = cours_string.split(" DTSTART:")
datesdecours[0] = datesdecours[0][8:]
datesdecours.sort()


for i in range(0, len(datesdecours)): #on cherche le prochain cours
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
#print(numerodecours)
#print(infocours)
#print(infocours[infocours.find("DESCRIPTION;"):infocours.find("\nEND")])#essai de traiter les données pour les mettre en libéllé de l'alarme

infocours = str(bla[numerodecours])
if datecoursdemain == demain : # On vérifie qu'on a cours demain, ça serait ballot quand même

    coursutc = datetime.datetime.strptime(datecoursdemain, '%Y%m%dT%H%M%SZ') #conversion de temps UTC à temps Local
    target_tz = pytz.timezone('Europe/Paris')
    local_tz = pytz.timezone('UTC')
    courshdp = local_tz.localize(coursutc)
    courshdp = target_tz.normalize(courshdp)

    alarm = (courshdp.hour * 60 + courshdp.minute) * 60 + courshdp.second #conversion en secondes

    datas=f"secret={utilisateur0.gmailsecret}&to={utilisateur0.gmailacc}&device=&priority=normal&payload={alarm-tempsdeglande}"
    requests.post('https://llamalab.com/automate/cloud/message',data=datas,headers={'content-type': 'application/x-www-form-urlencoded'}) #la requête finale !

"""dir_path = os.path.dirname(os.path.realpath(__file__))
path = f'{dir_path}/user'
for i in range(0,len(os.listdir())):
    if os.listdir()[i][:11]=="utilisateur":
        print(dossier)

    print(os.listdir()[i][:10])"""