from model.Hotelgast import Hotelgast
from model.Verblijfsperiode import Verblijfsperiode

class Hotel:
    Hotelgast = {}
    Verblijfsperiode = {}
    # for i in range (1, 17):
    #     __kamer_lijst = [i]
    # __kamer_lijst_b = []
    def __init__(self, _kamerlijst) -> None: #kamerlijst setter dictionary aanmaken
        self.kamerlijst = _kamerlijst

    @property
    def kamerlijst(self):
        return self.__kamerlijst

    @kamerlijst.setter
    def kamerlijst(self, value):
        kamerlijst1 = {self.__kamerlijst: self.__Hotelgast and self.__Verblijfsperiode}

        self.__kamerlijst = value

        super().__init__()

    def __str__(self) -> str:
        return super().__str__()