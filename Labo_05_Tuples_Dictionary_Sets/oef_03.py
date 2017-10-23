#oefening 3

nmct = {"1NMCT": "101", "2NMCT":"88", "3NMCT": "77"}
devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

#print(nmct) #{'1NMCT': 101, '2NMCT': 88, '3NMCT': 77}

#Een waarde van een dictionary opvragen
# print(nmct)
# print("Opvragen van een waard ahv de key")
# print(nmct.get("1NMCT"))

#Een element toevoegen aan een dicitonary
#nmct.update(Z="Hallo")
#print(nmct)

#een zelfde key aan de dictionary toevogen
#nmct.update({"1NMCT":"hallo"})
#print(nmct)
#De key wordt vervangen

#Controleren ofdat de key aanwezig is
# if "a" in nmct.keys():
#     print("De key is aanwezig")
# else:print("De key is niet aanwezig")

#een key met value cverwijderen
nmct.pop('1NMCT')
print(nmct)
