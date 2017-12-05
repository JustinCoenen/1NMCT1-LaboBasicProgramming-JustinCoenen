#oefening 11 gemeenschappelijke elementen

list1 = [78, 4, 5, 6, 4]
list2 = [89, 78, 4]

def geef_gemeenschappelijke_elementen(list1, list2):
    result = []
    for element in list1:
        if ((element in list2)and not (element in result)):
            result.append(element)
    return result
print (geef_gemeenschappelijke_elementen(list1, list2))
