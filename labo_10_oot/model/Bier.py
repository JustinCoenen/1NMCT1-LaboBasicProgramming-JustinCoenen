class Bier:
    def __str__(self) -> str:
        return super().__str__()

    def __init__(self, _nummer:int, _naam:str, _brouwerij:str, _alcohol:int, _kleur:str ) -> None:
        self.nummer = _nummer
        self.naam = _naam
        self.brouwerij = _brouwerij
        self.alcohol = _alcohol
        self.kleur = _kleur
    @property
    def nummer(self):
            return self.__nummer

    @nummer.setter
    def nummer(self, value):
        try:
            if value != "":
                self.__nummer = value
        except ValueError as exc:
            print("Foutmelding: Geen geldige nummer! {0}".format(exc))
        # else:
        #     print(value)
        #     self.__nummer = value
    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        try:
            if value != "":
                self.__naam = value
        except ValueError as exc:
            print("Geen geldige naam! {0}".format(exc))

    @property
    def brouwerij(self):
        return self.__brouwerij

    @brouwerij.setter
    def brouwerij(self, value):
        try:
            if value != "":
                self.__brouwerij = value
        except ValueError as exc:
            print("Ongeldige brouwerij naam! {0}".format(exc))

    @property
    def alcohol(self):
        return self.__alcohol

    @alcohol.setter
    def alcohol(self, value):
        try:
            if 0 > value <=100 and type(value) is float:
                self.__alcohol = value
            else:
                raise ValueError
        except ValueError as exc:
            print("Ongeldige alcohol percentage! {0}".format(exc))
        super().__init__()
    @property
    def kleur(self):
        return  self.__kleur

    @kleur.setter
    def kleur(self, value):
        try:
            if value != "":
                self.__kleur = value
        except ValueError as exc:
            print("Ongeldige kleur! {0}".format(exc))
        # else:
        #     print(value)