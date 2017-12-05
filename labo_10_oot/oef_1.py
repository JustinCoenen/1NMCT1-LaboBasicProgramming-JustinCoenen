#oefening 1
def lees_bestand():
    bestand = input("Geef een bestandnaam op:> ")
    try:
        fo = open(bestand)
        line = fo.readline()
        som = 0
        while line:
            try:
                line = line.rstrip("\n")
                som = som + int(line)
            except ValueError as exc:
                print("Lijn niet opgeteld: {0}".format(exc))
            finally:
                line = fo.readline()
        print(som)
    except FileNotFoundError as exc:
        print("Deze file bestaat niet: {0}".format(exc))
        fo.close()

lees_bestand()