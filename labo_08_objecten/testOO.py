# Importeren van boek

from Boek import Boek
from Auto import Auto
from Meetwiel import Meetwiel
from Winkelkar import Winkelkar
from Bier import Bier
import random

# boek1 = Boek("een titel", "uitgeverij", 123456, 2014)
# boek2 = Boek("iets", "uitgever", 56, 2020)
#
# print(boek1.titel)
#
# print(str(boek2.isbn) + " jaar: " + str(boek2.jaar))


# Oefening 3 -------------------------------------------------------------------


# om de volgorde te weten _kleur, _merk, _brandstof, _kmstand:int , _model


# autos = []
#
# porsche = Auto("rood", "Volkswagen", 1234,"sportwagen", "naft" )    #De class wordt opgeroepen
# tesla = Auto("zwart", "tesla", 1234, "elektrisch", "naft" )
#
# autos.append(porsche)
# autos.append(tesla)
#
# for auto in autos:
#     auto.rijden(random.randint(50, 850))
#     auto.brandstof = "iets"
#     print("De wagen is een {0} en heeft {1} kilometers afgelegd".format(auto.brandstof, auto.kmstand))

# MEETWIEL
# _straal:float =0, _omwentelingen:int =0

# meetwiel1 = Meetwiel(0.9, 10)
# print(meetwiel1.afstand)
# aantalomw=input("Geef extra aantal omwentelingen: ")
# extra_afstand = int(aantalomw) * meetwiel1.omtrek
# print(meetwiel1.afstand + extra_afstand)

# WinkelKar

# kar = Winkelkar()
# kar.voeg_product_toe("appel")
# kar.voeg_product_toe("peer")
# kar.voeg_product_toe("banaan")
#
# kar2 = Winkelkar()
# kar2.voeg_product_toe("aardappel")
# kar2.voeg_product_toe("water")
#
# print(kar.producten)
# print(kar2.producten)
#
# kar3 = Winkelkar()
#
# kar.tel_winkelkarren_op (kar2)
# print(kar.producten)
