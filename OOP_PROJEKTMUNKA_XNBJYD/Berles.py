class Berles:

    def __init__(self, kolcsonzes_id, autokolcsonzo, auto, datum, nev):
        self.kolcsonzes_id = kolcsonzes_id
        self.autokolcsonzo = autokolcsonzo
        self.auto = auto
        self.datum = datum
        self.nev = nev

    def get_kolcsonzesi_ar(self):
        return self.auto.get_kolcsonzesi_ar()

    def __str__(self):
        return f"Kölcsönzés #{self.kolcsonzes_id}: {self.nev} - {self.auto.get_leiras()} - Dátum: {self.datum.strftime('%Y-%m-%d')}"