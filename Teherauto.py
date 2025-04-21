from Auto import Auto

class Teherauto(Auto):

    def __init__(self, kolcsonzesi_ar, rendszam, tipus, ot_fos=False, nyitott_platos=False):
        super().__init__(kolcsonzesi_ar, rendszam, tipus)
        self.ot_fos = ot_fos
        self.nyitott_platos = nyitott_platos

    def get_leiras(self):
        ot_fos_info = "öt fős" if self.ot_fos else "három fős"
        nyitott_platos_info = "platós lehetőséggel" if self.nyitott_platos else "zárt terű"
        return f"Teherautó EBU-{self.rendszam}, {self.tipus} Iveco Daily, {ot_fos_info}, {nyitott_platos_info}, ár: {self.kolcsonzesi_ar} Ft/nap"