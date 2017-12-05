class Winkelkar:
    def __init__(self) -> None:
        self.__producten = [] #members
        super().__init__()

    @property
    def producten(self):
        return self.__producten

    #Methods
    def voeg_product_toe(self, nieuw_product):
        self.__producten.append(nieuw_product)

    def verwijder_product(self, product):
        self.__producten.remove(product)

    def tel_winkelkarren_op(self, winkelkar):
        #nieuwe derde kar
        w_result = Winkelkar()
        #lijsten optellen
        print(winkelkar.producten)
        for product in winkelkar.producten:
            self.producten.append(product)
        return(self.producten)

    def __str__(self) -> str:
        result = "De volgende winkelkarren bevatten: "
        return super().__str__()

    def __add__(self, other):
        return(self.producten + other.producten)