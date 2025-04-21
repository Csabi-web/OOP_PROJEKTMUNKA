class Autokolcsonzo:

    def __init__(self, nev, cim=""):
        self.nev = nev
        self.cim = cim
        self.autok = []

    def add_auto(self, auto):
        self.autok.append(auto)

    def get_auto(self, rendszam):
        for auto in self.autok:
            if auto.get_rendszam() == rendszam:
                return auto
        return None

    def get_autok(self):
        return self.autok