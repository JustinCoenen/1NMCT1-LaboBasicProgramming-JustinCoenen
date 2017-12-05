#oefening 6
# path = "bestanden/Scores.txt"
studenten_scores = {}
def inlezen_scores_studenten(path):
    fo = open(path, 'r')
    line = fo.readline()
    while (line):
        line = line.rstrip("\n")
        student_naam = line.split(":")[0]
        student_punten = line.split(":")[1:]
        studenten_scores[student_naam] = student_punten
        line = fo.readline()
    fo.close()

def geef_gemiddelde_scores(punten):
    return sum(punten)/len(punten)


def print_score(zoek_student):
    for naam in studenten_scores.keys():
        if (naam.lower().find(zoek_student.lower())!= -1):
            print("Gevonden naam: {0}".format(naam) + str(studenten_scores[naam]))

inlezen_scores_studenten("bestanden/Scores.txt")
print(print_score("Bo"))
# print(geef_gemiddelde_scores(studenten_scores.values()))
