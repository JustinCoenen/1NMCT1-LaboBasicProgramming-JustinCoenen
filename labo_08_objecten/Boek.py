
class Boek: #classes moeten met een hoofdletter beginnen | alt+insert voor __str__ en __init__
    def __str__(self) -> str:
        return super().__str__()

    #Dit is de constructor
    def __init__(self, _titel:str, _uitgeverij:str, _isbn:int, _jaar) -> None: #init is een constructor. parameters met _ beginnen
        self.titel = _titel
        self.uitgeverij = _uitgeverij
        self.isbn = _isbn
        self.jaar = _jaar

    #Properties (publiek) bestaat altijd uit een getter of read, setter of write
    @property
    def titel(self):
            return self.__titel #een getter
    def titel(self, value):
            self.__titel = value
    @property
    def uitgeverij(self):
            return self.__uitgeverij

    @uitgeverij.setter # <- mag er staan maar moet niet
    def uitgeverij(self, value):
            self.__uitgeverij = value
            #pass
    @property
    def isbn(self):
            return self.__isbn

    @isbn.setter
    def isbn(self, value):
            self.__isbn = value

    @property
    def jaar(self):
            return self.__jaar

    @jaar.setter #Bij setters kun je voorwaarden schrijven
    def jaar(self, value):
            if (value > 2017):
                value = 2017
                #self.__jaar = 2017
                print("Je maakt een fout")  #valitdatie
            self.__jaar = value