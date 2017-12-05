#oefening
import random
def get_random(my_list):
    rand_nmbr = random.randint(0, len(my_list)-1)
    return my_list[rand_nmbr]
    #korte methode
    #rand_nmbr = random.randint(0, len(my_list) - 1)
    #return my_list[random.randint(0, len(my_list) - 1)]
get_random(list)