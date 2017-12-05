#oef10

list1 = ["water", "aarde", "vuur", "lucht"]
list2 = ["water", "aarde", "vuur", "lucht"]

def zijn_verschillend(list1, list2):
    for item in list1:
        for i in list2:
            if item == i:
                return False
        else: return True


print (zijn_verschillend(list1, list2))