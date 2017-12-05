#applicatie voetbalspelers
import random
list_spelers = []

def inlezen_spelers(een_bestand): #In deze funtie worden de speles in de lijst 'list_spelers' gezet
    fo = open(een_bestand) #om een bestand te openen
    for speler in fo.readlines():
        list_spelers.append(speler)

def selecteer_elftal(een_lijst): #Hier worden er 11 spelers uitgezocht
    elftal=[]
    while len(elftal)<=10:
        index = random.randint(0, len(een_lijst)-1) #nummer vanaf 0 en de lengte van de lijst
        #TO DO: niet tweemaal dezelfde
        if not (een_lijst[index] in elftal):
            elftal.append(een_lijst[index])#Het random getal komt in de lijst totdat er 11 in de lijst zijn

    return elftal

def schrijf_naar_een_file (bron, target): #Hier worden de 11 spelers van de functie selecteer_elftal in een tekstbestand gestoken
    fo = open(target, "w")
    for speler in bron:
        fo.write(speler+"\n")


inlezen_spelers("bestanden/Spelers.txt")

print(list_spelers)

geselecteerd_elftal = selecteer_elftal(list_spelers)
schrijf_naar_een_file(geselecteerd_elftal, "spelers.txt")


#Foutmelding: list index out of range! python telt van 0(zero based) bij lengtes altijd en -1 toevoegen zie lijn 13