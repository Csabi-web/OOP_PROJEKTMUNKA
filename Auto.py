from abc import ABC, abstractmethod

class Auto(ABC):

    def __init__(self, kolcsonzesi_ar, rendszam, tipus):
        self.kolcsonzesi_ar = kolcsonzesi_ar
        self.rendszam = rendszam
        self.tipus = tipus

    @abstractmethod
    def get_leiras(self):
        pass

    def get_kolcsonzesi_ar(self):
        return self.kolcsonzesi_ar

    def get_rendszam(self):
        return self.rendszam

    def  get_tipus(self):
        return self.tipus