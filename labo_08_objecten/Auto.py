class Auto:
    def __init__(self, _kleur, _merk, _kmstand:int , _model, _brandstof:str ="naft") -> None:
        self.kleur = _kleur
        self.merk = _merk
        self.__brandstof = _brandstof  #memeber vvoor readonly
        self.model = _model
        self.kmstand = _kmstand
        # super().__init__()

    #read only properties -----------

    @property # read only heeft geen setter nodig
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        self.__kleur = value

    @property
    def kmstand(self):
        return self.__kmstand

    @kmstand.setter
    def kmstand(self, value):
        self.__kmstand = value

    #properties ----------------

    @property
    def merk(self):
        return self.__merk

    @merk.setter
    def merk(self, value):
        self.__merk = value
        # pass

    @property
    def brandstof(self):
        return self.__brandstof

    # @brandstof.setter
    # def brandstof(self, value):
    #     self.__brandstof = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    #methods----------
    def rijden(self, aantal_km):
        if aantal_km < 0:
            print("de km stand moet positief zijn")
        self.__kmstand += aantal_km

    def __str__(self) -> str:
        return "merk {0} van model {1} met kleur {2}".format(self.merk, self.model, self.kleur)
        return super().__str__()