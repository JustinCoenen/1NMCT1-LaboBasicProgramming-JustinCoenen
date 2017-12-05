#Tekstbestand toevoegen aan projectmap

#Voeg een tekstbestand toe aan uw projectmap.
#Voorzie het tekstbestand van verschillende regels tekst
#Maak nu een functie 'lees_bestand_in_met_lijnnummer" die het tekstbestand inleest en lijn per lijn afprint.
#Elke lijn wordt door een lijnnummer vooraf gegaan

def lees_bestand_in_met_lijnnummers(bestandsnaam):
    fo = open(bestandsnaam)
    line = fo.readline()
    index = 1

    while (line):
        line = line.rstrip("/n")
        print("{0} : {1}".format(index, line))
        line = fo.readline()
        index += 1

    fo.close()

lees_bestand_in_met_lijnnummers("tekstbestand.txt")
