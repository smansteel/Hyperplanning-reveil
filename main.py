import requests
import datetime
import pytz
transfert =""
D=[]
bla = []
datetrouvee = False
cours_string=""
def take_second(elem):
    return elem[:7]
mot =""
url= "https://planning-2021.isep.fr/Telechargements/ical/Edt_TARDIEU.ics?version=2018.0.3.1&idICal=EA705ABDB51740B2D372D527B5202649&param=643d5b312e2e36325d2666683d3126663d31"

def download_calendar():
    r = requests.get(url, allow_redirects=True)
    open('cal.ics', 'wb').write(r.content)


with open('cal.ics', 'r') as my_file:
    for ligne in my_file :
        transfert+= ligne
download_calendar
bla = transfert.split("BEGIN:VEVENT")
cours = []
for i in range(len(bla)):
    cours += tuple(bla[i].split("\n"))

for i in range(1,len(bla)-1):
    cours_string += bla[i].split("\n")[5] +" "

datesdecours = cours_string.split(" DTSTART:")
datesdecours.pop
datesdecours[0] =datesdecours[0][8:]
datesdecours.sort()
ajd = datetime.date.today().strftime("%Y%m%d")
demain_nf = datetime.date.today() + datetime.timedelta(days=1)
demain = demain_nf.strftime("%Y%m%d")


for i in range(0, len(datesdecours)):
    if datesdecours[i][:8]< demain :
        pass
    else :
        if datetrouvee == False :
            print(datesdecours[i])
            datecoursdemain = datesdecours[i]
            datetrouvee= True
        else :
            break

coursutc = datetime.datetime.strptime(datecoursdemain, '%Y%m%dT%H%M%SZ')
target_tz = pytz.timezone('Europe/Paris')
local_tz = pytz.timezone('UTC')
courshdp= local_tz.localize(coursutc)
courshdp = target_tz.normalize(courshdp)

print(courshdp)

