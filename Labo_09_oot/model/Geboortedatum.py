#Geboortedatum
import random
import datetime
class Geboortedatum:

    __aantal_data = 0  # <- teller

    def __str__(self) -> str:
        return("De geboortedatum: " + str(self.dag) + "/" + str(self.maand) + "/" + str(self.jaartal))
        # return super().__str__()

    def __init__(self, _dag:int, _maand:int, _jaartal:int) -> None: #VOLGORDE!!!!
        self.jaartal = _jaartal
        self.maand = _maand
        self.dag = _dag
        Geboortedatum.__aantal_data +=1

#Properties_______________________________________________________________________________

    @property
    def dag(self):
        return self.__dag

    @dag.setter
    def dag(self, value):
        if isinstance(value, int)and self.validate_dag(value):
            self.__dag = value
        else:
            self.__dag = None

    def validate_dag(self, _dag):
        if self.__maand in [1,3,5,7,8,10,12] and _dag <= 31:
            return True
        elif self.__maand in [4,6,9,11] and _dag <= 30:
            return True
        elif self.__maand == 2 and _dag <= 28:
            return True
        else:
            return False

    @property
    def maand(self):
        return self.__maand

    @maand.setter
    def maand(self, value):
        if isinstance(value, int) and value <= 12:
            self.__maand = value
        else:
            self.__maand = None

    @property
    def jaartal(self):
        return self.__jaartal

    @jaartal.setter
    def jaartal(self, value):
        if isinstance(value, int):
            self.__jaartal = value
        else:
            self.__jaartal = None



    @staticmethod
    def get_aantal_data():
        return Geboortedatum.__aantal_data

    @staticmethod
    def get_random_data():
        dag = random.randint(1, 28)
        jaartal = random.randint(1917, datetime.datetime.now().year)
        maand = random.randint(1, 13)
        return Geboortedatum(dag, maand, jaartal)

    @staticmethod
    def get_random_lijst_geboortedag(aantal:int):
        lijst_geboortedatum = []
        for i in range(0, aantal):
            lijst_geboortedatum.append(Geboortedatum.get_random_data())
        return lijst_geboortedatum

    #operator overloading ------------------------------

    def __eq__(self, other):
        if (self.jaar == other.jaar) and (self.maand==other.maand) and (self.dag == other.dag):
            return True
        else:
            return False

    def is_zelfde_verjaardag(self, andere_verjaardag): #Self is ook al een verjaardag
        if (self.__eq(self, andere_verjaardag)== True):
            return True
        else:
            return False
    # super().__init__()