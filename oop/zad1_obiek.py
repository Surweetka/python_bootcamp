class Produkt():
    def __init__(self, produkt, id, cena):
        self.produkt = produkt
        self.id = id
        self.cena = cena

    def product_info(self):
        print(f"Produkt: {self.produkt}, id: {self.id}, cena: {self.cena} PLN")

produkt1 = Produkt("kola", 4, 10.99)
produkt2 = Produkt("woda", 1, 2)
produkt1.product_info()
produkt2.product_info()
