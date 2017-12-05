#oefening 8
my_list = [12,5,6]
def som_num_in_list(my_list):
    sum = 0
    for number in my_list:
        sum = sum + number
    return sum




print("De som is {0}".format(som_num_in_list(my_list)))