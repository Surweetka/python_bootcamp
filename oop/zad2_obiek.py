from test import Osoba

class Employee():
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.godziny = 0

    def register_time(self, godziny):
        self.godziny += godziny
        if godziny > 8:
            self.godziny += godziny - 8

    def pay_salary(self):
        wyplata = self.stawka * self.godziny
        self.godziny = 0.0
        return wyplata

employee1 = Employee("Jan", "Nowak", 100.0)
print(employee1.pay_salary())
employee1.register_time(5)
employee1.register_time(10)
print(employee1.pay_salary())
print(employee1.pay_salary())