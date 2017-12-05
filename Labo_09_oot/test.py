from model.Speler import Speler
from model.Geboortedatum import Geboortedatum
speler1 = Speler("naam", "voornaam", 2, Geboortedatum.get_random_data())
speler2 = Speler("Peter2", "Vandenbroucke2", 3, Geboortedatum.get_random_data())
speler3 = Speler("Peter3", "Vandenbroucke3", 4, Geboortedatum.get_random_data())


#print(speler1)
#print(Speler.get_team_score()) # telt alle scores op van Speler1, Speler2 en Speler3

list_spelers = [speler1, speler2, speler3]
# for speler in list_spelers:
#     print("Speler {0} geboren op {1}".format(speler, str(speler.geboortedatum)))

#print(list_spelers)


geboortedatum1 = Geboortedatum(12, 4, 2000)
geboortedatum2 = Geboortedatum(14, 1, 1956)
geboortedatum3 = Geboortedatum.get_random_data()
geboortedatum4 = Geboortedatum.get_random_lijst_geboortedag(4)

for geboortedatum in geboortedatum4:
    print("{0}".format(str(geboortedatum)))

# print(geboortedatum1)
# print(geboortedatum2)
# print(geboortedatum3)
print(geboortedatum4)