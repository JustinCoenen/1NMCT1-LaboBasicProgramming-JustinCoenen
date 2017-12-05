#oefening 2 lijst aanvullen tot
list_vrienden = []
new_friend = "Joke"
while (new_friend!=""):
    new_friend = input("Ga en zoek naar ...")

    if (new_friend!=""):
        print(new_friend)
        list_vrienden.append(new_friend)
    else:
        print("Mijn vrienden noemen {0}".format(list_vrienden))