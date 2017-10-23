#oefening 4

nmct = {"1NMCT": "101", "2NMCT":"88", "3NMCT": "77"}
devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

def print_dictionary(name, nmct):
    print("Dit zijn de keys en values uit de dictionary: ")
    for key, value in nmct.items():
        print("Key: %s -> value: %s." % (key, value))

print_dictionary("NMCT", nmct)