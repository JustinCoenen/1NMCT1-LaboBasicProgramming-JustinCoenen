#Oefen 3 vul een bestand aan

import os
def vul_bestand_aan(een_bestand):
    fw = open(een_bestand, "a+" ) #Om er iets aan toe te voegen
    while True:
        lijn = input("Geef een nieuwe lijn in of stop met 's'. ")
        if lijn == 's':
            break
        else:
            fw.write(lijn + "\n") #om een nieuwe regel an toe te voegen
    fw.close()

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
    vul_bestand_aan("bestanden/test2t.txt")
else:
    schrijf_bestand("bestanden/test2t.txt")
