class Zwierz():
    def przedstaw_sie(self):
        print("Nie wiem czym jestem")


class Pies(Zwierz):
    def przedstaw_sie(self):
        print("Jestem psem")


z = Zwierz()
z.przedstaw_sie()
