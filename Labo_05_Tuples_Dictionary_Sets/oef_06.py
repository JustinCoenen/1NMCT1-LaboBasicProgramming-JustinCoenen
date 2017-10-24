#oefening 6

howest = {"1NMCT": 101, "2NMCT":88, "3NMCT": 77, "1Devine": 123, "2Devine": 98, "3Devine": 55, "1IPO":51}
def voeg_nieuw_element_toe(akey, value, dict):
    print (akey)
    print("Dit zijn de keys en values uit de dictionary: ")
    for akey, value in howest.items():
        print("Key: %s -> value: %s." % (akey, value))
    if not akey in howest:
        print("Ok")
        dict.update({akey:value})
    else:
        print("not ok")


voeg_nieuw_element_toe("1NMCT", 30, howest)