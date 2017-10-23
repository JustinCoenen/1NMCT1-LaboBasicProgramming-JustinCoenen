#oef2

tuple1 = ("1NMCT", "2NMCT", "3NMCT")
tuple2 = ("1Devine", "2Devine", "3Devine")
#tuple3 = ("Test", True, 3.2)

def print_tuple(name, tuple):
        print("Dit is de lijst van {0}:".format(name))
        for element in tuple:
            print("{0} zit op positie {1}".format(element, tuple.index(element)))

print_tuple("MCT", tuple1)