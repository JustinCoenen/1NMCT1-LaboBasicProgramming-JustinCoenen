from model.Hotel import Hotel
from model.Hotelgast import Hotelgast
from model.Verblijfsperiode import Verblijfsperiode

Hotelgast.naam = input(str("Geef naam: "))
Hotelgast.voornaam = input(str("Geef voornaam: "))
Hotelgast.adres = input(str("Geef adres: "))
Verblijfsperiode.startdatum = input(str("Geef startdatum: "))
Verblijfsperiode.einddatum = input(str("Geef einddatum: "))
Hotel.kamerlijst = Hotel.kamerlijst

# print(Hotelgast.naam)
# print(Hotelgast.voornaam)
# print(Hotelgast.adres)
# print(Verblijfsperiode.startdatum)
# print(Verblijfsperiode.einddatum)
print(Hotel.kamerlijst)