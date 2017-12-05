#oefening 7 max getallen

def get_max(my_list):
     max_nmbr = 0
     for element in my_list:
         if (element >max_nmbr):
             max_nmbr=element
     return max_nmbr


lst_nmbrs = [1, 2, 2000, 3000, -5000, 150000] #korte manier
print(max(lst_nmbrs))

print(get_max(lst_nmbrs))