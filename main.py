import requests


url= "https://planning-2021.isep.fr/Telechargements/ical/Edt_TARDIEU.ics?version=2018.0.3.1&idICal=EA705ABDB51740B2D372D527B5202649&param=643d5b312e2e36325d2666683d3126663d31"

def download_calendar():
    r = requests.get(url, allow_redirects=True)
    open('cal.ics', 'wb').write(r.content)

with open('cal.ics', 'r') as my_file:
    my_file.read