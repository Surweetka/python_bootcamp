class Przedmiot():
    def __init__(self, nazwa, bonusy_do_ataku):
        self.nazwa = nazwa
        self.bonusy_atk = bonusy_do_ataku

    def __str__(self):
        return f"{self.nazwa}, {self.bonusy_atk} do ataku"