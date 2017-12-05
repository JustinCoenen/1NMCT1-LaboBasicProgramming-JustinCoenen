#list days of the week

list = ["ma", "di", "wo", "do", "vrij", "za", "zo"]

print(list)
print(list[0:5]) #range buitekant neemt hij nooit mee
print(list[5:])
print(list[0:7:2])
print(list[1:7:2])

import random
def get_random(my_list):
    rand_nmbr = random.randint(0, len(my_list)-1)
    return my_list[rand_nmbr]

get_random(list)
print(get_random(list))