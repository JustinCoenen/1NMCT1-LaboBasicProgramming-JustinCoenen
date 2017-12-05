from model.Geboortedatum import Geboortedatum

class Speler:
    #private static variable
    __score_team = 0


    def __init__(self, _naam, _voornaam, _score:int, _geboortedatum = Geboortedatum(4, 12, 1968)) -> None:
        self.naam = _naam
        self.voornaam = _voornaam
        self.score = _score
        self.geboortedatum = _geboortedatum

    @property
    def naam(self):
            return self.__naam

    @naam.setter
    def naam(self, value):
            self.__naam = value

    @property
    def voornaam(self):
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        self.__voornaam = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if isinstance(value, int):
            self.__score = value
            Speler.__score_team += value
        else:
            self.__score = 0

    @staticmethod
    def get_team_score():
        return Speler.__score_team

#Methods--------------------



    def __str__(self) -> str:
        return ("De speler {0} heeft score {1} {2}.".format(self.__naam, self.__score, self.geboortedatum))
        # return super().__str__()