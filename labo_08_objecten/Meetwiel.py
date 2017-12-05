import math
class Meetwiel:
    def __init__(self, _straal:float =0, _omwentelingen:int =0) -> None:
        self.straal = _straal
        self.omwentelingen = _omwentelingen
        super().__init__()

    #properties

    @property
    def straal(self):
        return self.__straal

    @straal.setter
    def straal(self, value):
        self.__straal = value

    @property
    def omwentelingen(self):
        return self.__omwentelingen

    @omwentelingen.setter
    def omwentelingen(self, value):
        self.__omwentelingen = value

    #methods
    @property
    def omtrek(self):
        return 2*self.__straal*math.pi

    @property
    def afstand(self):
        return self.__omwentelingen * self.omtrek

    def __str__(self) -> str:
        return super().__str__()