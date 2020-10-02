from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

session = Session()
session.auth = HTTPBasicAuth("mata61382", "Sman_steel01")

lPrefixeWsdl='http://planning-2021.isep.fr/hpsw/wsdl/'

# Interfaces utilisées
Matiere = Client(lPrefixeWsdl + 'IHpSvcWMatieres', transport=Transport(session=session))
Admin = Client(lPrefixeWsdl + 'IHpSvcWAdmin', transport=Transport(session=session))

# Affichage de la version
print ('Connecté à ' + Admin.service.Version());
    
# Affichage du nombre de matières
print ('Il y a ' + str(Matiere.service.NombreMatieres()) + ' matières dans la base ');

# Affichage de la liste des matières
lCles = Matiere.service.TrierTableauDeMatieresParLibelleEtCode ({'THpSvcWCleMatiere' : Matiere.service.ToutesLesMatieres()});
lClesIn = {'THpSvcWCleMatiere' : lCles};
lCodes = Matiere.service.CodesTableauDeMatieres(lClesIn);
lLibelles = Matiere.service.LibellesTableauDeMatieres(lClesIn);
lLibellesLongs = Matiere.service.LibellesLongsTableauDeMatieres(lClesIn);

for i in range (len (lCles)): 
    print (str(lCles[i]) + ' '  + str(lCodes[i] if lCodes[i] is not None else '') + ' '  + str(lLibelles[i]) + ' : '  + str(lLibellesLongs[i] if lLibellesLongs[i] is not None else '-'))
