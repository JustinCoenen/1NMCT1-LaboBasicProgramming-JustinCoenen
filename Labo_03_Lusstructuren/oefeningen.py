# Labo_les_03

# oef 1
# number = 100
# my_sum = 0
#
# for index in range(1, 100):
#     print(index)
#     my_sum = my_sum + index
#
# print(my_sum)

# oef 2

# for index in range(20, 51):
#     print(index)

# oef 3

# for index in range (4, 100):
#     if (index%2==0):
#         print(index)

# oef 4
# for index in range (10, 109):
#     if (index%2 == 1):
#         print(index)

# oef 5 :LET OP: laatste getal niet meegenomen!
# for index in range (99, -1, -3):
#     print(index)

# oef 6
# for index in range (200, 309):
#     if (index%7 == 0)and(index%5!=0):
#         print(index)

# oef 7

# def print_lijst_getallen(startgetal, aantal, stap):
#      end= startgetal + aantal * stap
#      for index in range(startgetal, end, stap):
#          print(index)
#
# stap = int(input("Hoe groot is je stap? "))
# startgetal = int(input("Geef een startgetal: "))
# aantal = int(input("Hoeveel getallen? "))
#
# print_lijst_getallen(startgetal, aantal, stap)

# oef 8

# index=1
# som=0
# while index< 100:
#     som=som+index
#     index +=1
# print("De som is {0}".format(som))

# oef 9
# import random
#
# random_getal = int(random.random()*20) #getal tussen 0 en 20
# gok = int(input("Raad een getal tussen 1 en 20: "))
#
# while (gok != random_getal):
#     tekst = ""
#     if (gok > random_getal):
#         tekst = "Getal te groot. "
#     else:
#         tekst = "Getal is te klein. "
#     gok = int(input("{0}Probeer opnieuw: ".format(tekst)))
# else:
#     print("Goed geraden!")

# oef 10

# import calendar
#
#
#
# jaar_start = int(input("Geef een start jaar op: "))
# jaar_end = int(input("Geef een eind jaar op: "))
#
# for index in range(jaar_start, jaar_end):
#     if (calendar.isleap(index)):
#         (print("{0} is een schrikkeljaar".format(index)))
#     else:
#         print("{0} is geen schrikkeljaar".format(index))

# oef 12 priemgetal
#
# def is_priem(getal):
#     for teller in range(2, getal):
#         if(getal % teller == 0):
#             return False
#     return True
#
# for teller in range(1, 100):
#     print(str(teller) + is_priem(teller))

# faculteit via recursief werken
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact (x - 1)
#
# x = int(input("Geef een positief geheel getal op: "))
# print("De faculiteit van %d is %d" % (x, fact(x)))

# print("Justin" [1:2]) #Hier zal bv alleen maar "u" weergegeven

# def swap(woord1, woord2):
#     deel1 = woord1[0:2] + woord2 [2:]
#     deel2 = woord2[0:2] + woord1 [2:]
#     return "{0} {1}".format(deel2, deel1)
#
# #functie oproepen
# print(swap("abc", "xyz"))

# def genereer_paswoord(naam, voornaam, geboortejaar):
#     naam = naam.lower()[0:3]
#     voornaam = voornaam.upper()[0:2]
#     geboortejaar = geboortejaar[3:5] + geboortejaar[8:10]
#     return naam + voornaam + geboortejaar
#
#
# naam = input("Geef je naam op: ")
# voornaam = input("Geef je voornaam op: ")
# geboortejaar = input("Geef je geboortedatum op (dd-mm-yyyy): ")
#
# print(genereer_paswoord(naam, voornaam, geboortejaar))

#oef e-mail
#import email

# def check_email(email):
#     if email.endswith("@student.howest.be"):
#         print("Dit is een geldig e-mail adres.")
#     else:
#         print("Niet geldig.")
#
#
# mail = str(input("Geef uw Howest e-mail adres op: "))
#
# check_email(mail)

def wachtwoord(minimum_lengte, maximum_lengte):
    