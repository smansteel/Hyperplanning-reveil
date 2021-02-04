#les imports tout propres
import requests
import datetime
import pytz
import os
from utilisateur0 import *



transfert = ""
D = [""]
bla = []
datetrouvee = False
cours_string,lieustring = "", ""
ajd = datetime.date.today().strftime("%Y%m%d")
demain_nf = datetime.date.today() + datetime.timedelta(days=1)
demain = demain_nf.strftime("%Y%m%d")
cours = []
dossier = os.listdir()

url = url_calendrier



def download_calendar():
    r = requests.get(url, allow_redirects=True)
    open('cal.ics', 'wb').write(r.content)
    print("cal updated")

download_calendar()
with open('cal.ics', 'r') as my_file: #hopla gros bourrin on met tout dans un string
    for ligne in my_file:
        transfert += ligne

temp = transfert.split("BEGIN:VEVENT")
for i in range(0, len(temp)):
    bla += " "
for i in range(0,len(temp)):
    etatcours = temp[i][temp[i].find("UID:")+4:temp[i].find("TARDIEU")-8]
    if etatcours[1]== "o":
        bla[i] = temp[i]


for i in range(len(bla)):
    cours += tuple(bla[i].split("\n"))
for i in range(0,28):
    bla.pop()

for i in range(1, len(bla) - 1):
    cours_string += bla[i].split("\n")[5] + " " #C'est ici le parsing des infos
    lieustring += bla[i].split("\n")[8] + " "

removelist =[]

datesdecours = [cours_string.split("DTSTART:"),lieustring.split("LOCATION;LANGUAGE=fr:")]
"""'for i in range(0,len(datesdecours)):
    if len(datesdecours[0][i]) == 8:
        removelist += datesdecours[0][i]'"""

lieudecours = lieustring.split("LOCATION;LANGUAGE=fr:")


datesdecours[0].sort()


for i in range(0, len(datesdecours[0])): #on cherche le prochain cours
    if datetrouvee == False and datesdecours[0][i][:8] == demain:
        datecoursdemain = datesdecours[0][i]
        lieu_cours = datesdecours[0][i]
        datetrouvee = True

for i in range(0,len(bla)):
    if datecoursdemain[:8] in temp[i].split("\n")[5]:
        numerodecours = i


infocours = str(bla[numerodecours])


coursutc = datetime.datetime.strptime(datecoursdemain, '%Y%m%dT%H%M%SZ ') #conversion de temps UTC à temps Local

target_tz = pytz.timezone('Europe/Paris')
local_tz = pytz.timezone('UTC')
courshdp = local_tz.localize(coursutc)

courshdp = target_tz.normalize(courshdp)
alarm = (courshdp.hour * 60 + courshdp.minute) * 60 + courshdp.second #conversion en secondes

if "Teams" in bla[numerodecours]:
    msg = msg_maison
    wakeuptime = temps_maison
elif "NDC" in bla[numerodecours]:
    msg = msg_ndc
    wakeuptime = temps_ndc
elif "NDL" in bla[numerodecours]:
    msg = msg_ndl
    wakeuptime = temps_ndl
with open("horaires.txt", "w") as horaires:
    horaires.write(str(wakeuptime))
    horaires.write("\n")
    horaires.write(str(msg))
    print(wakeuptime, msg)