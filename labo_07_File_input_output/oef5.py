#Morsevertaling

morse_dict = {}

def lees_morse_file_in(bestandsnaam):
    fo = open(bestandsnaam)
    line = fo.readline()
    line = fo.readline()
    while line:
        line = line.rstrip("\n")
        key = line.split (";")[0]
        value = line.split (";")[1]
        morse_dict[key] = value
        line = fo.readline()
    fo.close


def vertaal_letter(een_letter):
    een_letter = een_letter.lower()
    if een_letter in morse_dict.keys():
        return morse_dict[een_letter]
    else:
        return "?"

def vertaal_naar_morse(een_tekst):
    vertaling=""
    for letter in een_tekst:
        vertaling += vertaal_letter(letter)
    return vertaling



lees_morse_file_in("bestanden/MorseVertaling.txt")
#print(morse_dict)
print(vertaal_naar_morse("Een tekst om te vertalen"))
