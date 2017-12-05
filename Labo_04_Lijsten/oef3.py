#Oefening 3 a list of numbers

lst_numbers = []

for nmbr in range (1,485,23):
    lst_numbers.append(nmbr)

print(lst_numbers)
lst_numbers.reverse()
print(lst_numbers)
lst_numbers.remove(24)
print(lst_numbers [len(lst_numbers)-1])