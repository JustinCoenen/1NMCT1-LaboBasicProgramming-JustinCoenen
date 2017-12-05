#oefenning 2

from labo_08_objecten.Bier import Bier
bier1 = Bier(23, "NMCT", "Howest", 5.2, "bruin")

try:
    bier1.naam = input("Geef een nieuwe bier naam: ")
except ValueError as exc:
    print("Forumelding! Geen geldige naam")

print(bier1)

#thuis nog de andere doen
