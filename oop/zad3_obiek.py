class ElectricCar():
    def __init__(self, zasieg):
        self.zasieg = zasieg
        self.droga = self.zasieg

    def drive(self, odleglosc):
        wynik = self.zasieg - odleglosc
        if wynik < 0:
            wynik = self.zasieg
            self.zasieg = 0
            return wynik
        else:
            self.zasieg -= odleglosc
            return odleglosc

    def charge(self):
        self.droga = self.zasieg


car = ElectricCar(100)
print(car.drive(70))
print(car.drive(50))
print(car.drive(20))
print(car.droga)
car.charge()
print(car.droga)
