#oefening 12

list1=['A', 89, 78, 4, 'A', 'test', 4]
#list2=['A', 89, 78, 4, 'A', 'test', 4]


def verwijder_duplicaten(list1):
    delete = [] #zonnder duplicaten
    for element in list1:
        if element not in delete:
            delete.append(element)
            print("delete"+str(delete))
    return delete
    #print(list1)
    #print(delete)

print (verwijder_duplicaten(list1))