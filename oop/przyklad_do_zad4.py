from random import randint
from przedmiot import Przedmiot


class Postac():
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self.atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []

    # def przedstaw_sie(self):
    #     print(self)

    def atak(self):
        wynik = self.atak
        for p in self.ekwipunek:
            wynik += p.bonus_atk
        return wynik

    def __str__(self):
        if self.czy_zyje():
            napis = "EKWPIUNEK:\n"
            for x in self.ekwipunek:
                napis += str(x) + "\n"
            return f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.\n" + napis
        else:
            return f"Jestem {self.imie}, miałem {self.atak} i nie żyję."

    def obrazenia(self, ile):
        print(f"{self.imie} oberwał za {ile} obrażeń.")
        self.zdrowie = self.zdrowie - ile
        if self.zdrowie < 0:
            self.zdrowie = 0

    def czy_zyje(self):
        return self.zdrowie > 0

    def heal(self):
        if self.zdrowie > 0:
            leczenie = randint(5, 25)
            self.zdrowie = self.zdrowie + leczenie
            print(f"{self.imie} użył zdolności leczących + {leczenie} HP")
            print(f"Zdrowie {self.imie} {self.zdrowie}/{self.max_zdrowie}")
        else:
            pass
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = self.max_zdrowie

    def unik(self):
        pass

    def moc_ataku(self):
        wynik = randint(self.atak // 2, self.atak)
        return wynik

    def daj_przedmiot(self):
        self.ekwipunek.append(przedmiot)

    def atak_plus(self):
        wynik = self.atak
        for p in self.ekwipunek:
            wynik += p.bonus_atk
        return wynik

    @staticmethod
    def walka(atakujacy, broniacy):
        print(f"Walka: {atakujacy.imie} vs {broniacy.imie}")
        while atakujacy.czy_zyje() and broniacy.czy_zyje():
            print(atakujacy)
            print(broniacy)
            atak_atakujacego = atakujacy.moc_ataku()
            atak_broniacego = broniacy.moc_ataku()
            print(f"{atakujacy.imie} uderza {broniacy.imie} za {atak_atakujacego} obrażeń.")
            broniacy.obrazenia(atak_atakujacego)
            print(f"{broniacy.imie} uderza {atakujacy.imie} za {atak_broniacego} obrażeń.")
            atakujacy.obrazenia(atak_broniacego)
        print("KONIEC WALKI")


tomasz = Postac("Tomasz", 35, 100)
stanley = Postac("Stanley", 25, 200)

tulipan = Przedmiot("Zielony tulipan zniszczenia", 5)
tomasz.daj_przedmiot(tulipan)

Postac.walka(tomasz, stanley)
print(tomasz)
print(stanley)

print(f"bonus atk: {tomasz.atak_plus()}")

# print(tomasz)
# print()
# tomasz.obrazenia()
# print()
# tomasz.czy_zyje()
# print()
# tomasz.heal()
# print()
# tomasz.obrazenia()
# print()
# print(tomasz)


# def test_nowa_postac():
#     postac = Postac("Adam", 1, 25)
#
#     assert postac.imie == "Adam" and postac.atak == 1 and postac.zdrowie == 25 and postac.max_zdrowie == 25


# def test_obrazenia():
#     postac = Postac("Rolewski", 4, 200)
#     assert postac.zdrowie == 200
#     postac.obrazenia(80)
#     assert postac.zdrowie == 120
#     postac.obrazenia(200)
#     assert postac == 0
