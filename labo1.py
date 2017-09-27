#oefening 4: seconden omzetten

#time = int(input("Geef mij een aantal seconden:"))
#print(type (time)) #string -> int

#day = time/(24*60*60)
#print (day)
#time = time % (24*60*60)
#hour = time/60*60
#time = time %3600
#time %= 3600 #verkorte manier van schrijven
#minutes = time/60
#time %= 60
#seconds = time


#print ("d:h:m:s -> {0:.0f}:{1:.0f}:{2:.0f}:{3:.0f}".format(day, hour, minutes, seconds))
#print("day:hour:minutes:seconds {0} {1} {2} {3}".format(day, hour, minutes, seconds))


#Oefening 5: bereken de som

number = (input("Geef mij een getal: "))
n = int(number)
nn= int(2 * number)
nnn= int( 3 * number)

print(n + nn + nnn)
