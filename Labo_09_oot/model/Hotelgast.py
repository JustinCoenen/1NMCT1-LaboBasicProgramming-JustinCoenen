

class Hotelgast:
    def __init__(self, _naam, _voornaam, _adres) -> None:
        self.naam = _naam
        self.voornaam = _voornaam
        self.adres = _adres

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
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, value):
        self.__adres = value
        super().__init__()

    def __str__(self) -> str:
        return super().__str__()