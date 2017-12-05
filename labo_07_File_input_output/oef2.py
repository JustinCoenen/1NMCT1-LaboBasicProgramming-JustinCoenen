#oefening 2

import os
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

def schrijf_bestand(een_bestand):
    fw = open(een_bestand , "w") #overschrijft !!
    while True:
        lijn = input("Geef een nieuwe lijn in of stop met 's'. ")
        if lijn == 's':
            break
        else:
            fw.write(lijn + "\n") #om een nieuwe regel an toe te voegen
    fw.close()


if os.path.exists("bestanden/test2t.txt"):
    lees_bestand_in_met_lijnnummers("bestanden/test2t.txt")
else:
    schrijf_bestand("bestanden/test2t.txt")