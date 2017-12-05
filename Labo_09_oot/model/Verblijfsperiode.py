

class Verblijfsperiode:
    def __init__(self, _startdatum, _einddatum) -> None:
        self.startdatum = _startdatum
        self.einddatum = _einddatum


    @property
    def startdatum(self):
        return self.__startdatum

    @startdatum.setter
    def startdatum(self, value):
        self.__startdatum = value

    @property
    def einddatum(self):
        return self.__einddatum

    @einddatum.setter
    def einddatum(self, value):
        self.__einddatum = value
        super().__init__()

    def __str__(self) -> str:
        return super().__str__()