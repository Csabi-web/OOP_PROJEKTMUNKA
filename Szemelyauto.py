from Auto import Auto

class Szemelyauto(Auto):

    def __init__(self, kolcsonzesi_ar, rendszam, tipus, Cabrio=False):
        super().__init__(kolcsonzesi_ar, rendszam, tipus)
        self.Cabrio = Cabrio

    def get_leiras(self):
        Cabrio_info = "kabrió" if self.Cabrio else "zárt terű"
        return f"Személyautó EBU-{self.rendszam},{self.tipus} Opel Astra {Cabrio_info}, ár: {self.kolcsonzesi_ar} Ft/nap"


