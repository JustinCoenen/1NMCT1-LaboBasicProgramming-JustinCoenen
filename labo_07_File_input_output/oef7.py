#JSON files
import requests

def download():
    params = {'format': 'json', 'language': 'nl'}
    response = requests.get("https://data.kortrijk.be/sport/outdoorlocaties.json", params)
    if response.status_code == 200:
        response_json = response.json() #JSON-File uit body ophalen
        print(response_json)
        return response_json
    else:
        return None

def geef_namen_outdoor_locaties(outdoor):
    fo = open(outdoor)
    openluchtinfra = []
    for i in outdoor:
        openluchtinfra.append(i)
        return set(openluchtinfra)


print (download())
print(geef_namen_outdoor_locaties())