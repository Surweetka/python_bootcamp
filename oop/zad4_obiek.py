from zad1_obiek import Produkt


class BasketEntry():
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.cena * self.quantity

class Basket():
    def __init__(self, koszyk):
        self.entries = []


    def add_product(self, product, qty):
        self.entries.append(BasketEntry(product, qty))

    def count_total_price(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.product.cena * entry.quantity
        return total_price

    def generate_report(self):
        pass

pr1 = Produkt(1, "Woda", 2)
basket = Basket()
basket.add_product(pr1, 4)
assert basket.count_total_price() == 8