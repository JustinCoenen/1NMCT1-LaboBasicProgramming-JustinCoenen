#oefening 09
import math
my_list = [122, 144, 129, 126]

def gemiddelde_in_list(my_list):
    som = 0
    for number in my_list:
        som = som + number
    gemiddelde = som/4
    return gemiddelde

print(gemiddelde_in_list(my_list))

