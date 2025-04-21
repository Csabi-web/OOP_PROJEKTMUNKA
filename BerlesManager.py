from datetime import datetime, timedelta
from Berles import Berles
from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto

class BerlesManager:

    def __init__(self):
        self.kolcsonzesek = []
        self.kovetkezo_kolcsonzes_id = 1

    def kolcsonzes_letrehozasa(self, autokolcsonzo, rendszam, datum, nev):
        if datum < datetime.now().date():
            return None, "Csak jövőbeli dátumon lehet kölcsönözni!"

        auto = autokolcsonzo.get_auto(rendszam)
        if not auto:
            return None, f"A {rendszam} számú autó nem létezik!"

        for kolcsonzes in self.kolcsonzesek:
            if kolcsonzes.auto.get_rendszam() == rendszam and kolcsonzes.datum == datum:
                return None, f"A {rendszam} számú autó már kölcsönözve van ezen a napon: {datum.strftime('%Y-%m-%d')}"

        kolcsonzes = Berles(self.kovetkezo_kolcsonzes_id, autokolcsonzo, auto, datum, nev)
        self.kolcsonzesek.append(kolcsonzes)
        self.kovetkezo_kolcsonzes_id += 1

        return kolcsonzes, None

    def kolcsonzes_lemondasa(self, kolcsonzes_id):
        for i, kolcsonzes in enumerate(self.kolcsonzesek):
            if kolcsonzes.kolcsonzes_id == kolcsonzes_id:
                torolt_kolcsonzes = self.kolcsonzesek.pop(i)
                return torolt_kolcsonzes, None

        return None, f"A {kolcsonzes_id} azonosítójú kölcsönzés nem létezik!"

    def osszes_kolcsonzes_listazasa(self):
        return self.kolcsonzesek

    def autokolcsonzesek_listazasa(self, rendszam):
        return [kolcsonzes for kolcsonzes in self.kolcsonzesek if kolcsonzes.auto.get_rendszam() == rendszam]


def rendszer_inicializalasa():
    autokolcsonzo = Autokolcsonzo("Csaba autó-kölcsönzője", "Siófok, Fürdő utca 23.")

    autokolcsonzo.add_auto(Szemelyauto(45000, 123, 1.4, Cabrio=True))
    autokolcsonzo.add_auto(Szemelyauto(22000, 234, 1.6,  Cabrio=False))
    autokolcsonzo.add_auto(Teherauto(25000, 345, 2.5, ot_fos=True, nyitott_platos=True))

    kolcsonzes_manager = BerlesManager()
    ma = datetime.now().date()
    holnap = ma + timedelta(days=1)
    egy_het_mulva = ma + timedelta(days=7)
    ket_het_mulva = ma + timedelta(days=14)

    kolcsonzes_manager.kolcsonzes_letrehozasa(autokolcsonzo, 123456, ma, "Csizmadia Csaba")
    kolcsonzes_manager.kolcsonzes_letrehozasa(autokolcsonzo, 234, ma, "Jakab Sándor")
    kolcsonzes_manager.kolcsonzes_letrehozasa(autokolcsonzo, 345, ma, "Tóth József")
    kolcsonzes_manager.kolcsonzes_letrehozasa(autokolcsonzo, 234, ma, "Kiss Evelin")
    kolcsonzes_manager.kolcsonzes_letrehozasa(autokolcsonzo, 123, ma, "Nagy István")

    return autokolcsonzo, kolcsonzes_manager


def datum_bekerese():
    while True:
        try:
            datum_str = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
            return datum
        except ValueError:
            print("Érvénytelen dátumformátum. Kérem, használja az ÉÉÉÉ-HH-NN formátumot.")


def menu_megjelenites():
    print("\n" + "=" * 50)
    print(" AUTÓ-KÖLCSÖNZŐ RENDSZER")
    print("=" * 50)
    print("1. Autók listázása")
    print("2. Kölcsönzés létrehozása")
    print("3. Kölcsönzés lemondása")
    print("4. Kölcsönzések listázása")
    print("0. Kilépés")
    print("=" * 50)


def main():
    autokolcsonzo, kolcsonzes_manager = rendszer_inicializalasa()
    while True:
        menu_megjelenites()
        valasztas = input("Válasszon műveletet (0-4): ")

        if valasztas == "0":
            print("Köszönjük, hogy használta a rendszert! Viszontlátásra!")
            break

        elif valasztas == "1":
            print("\nElérhető autók az autókölcsönzőben:")
            for auto in autokolcsonzo.get_autok():
                print(auto.get_leiras())

        elif valasztas == "2":
            print("\nKölcsönzés létrehozása:")
            print("Elérhető autók:")
            for auto in autokolcsonzo.get_autok():
                print(auto.get_leiras())

            rendszam = input("Adja meg a rendszámot: ")
            try:
                rendszam = int(rendszam)
            except ValueError:
                print("Érvénytelen rendszám!")
                continue

            datum = datum_bekerese()
            nev = input("Adja meg a kölcsönző nevét: ")

            kolcsonzes, hiba = kolcsonzes_manager.kolcsonzes_letrehozasa(autokolcsonzo, rendszam, datum, nev)

            if kolcsonzes:
                print(f"Kölcsönzés sikeresen létrehozva! Azonosító: {kolcsonzes.kolcsonzes_id}")
                print(f"Fizetendő összeg: {kolcsonzes.get_kolcsonzesi_ar()} Ft")
            else:
                print(f"Hiba a kölcsönzés létrehozásakor: {hiba}")

        elif valasztas == "3":
            print("\nKölcsönzés lemondása:")
            try:
                kolcsonzes_id = int(input("Adja meg a lemondani kívánt kölcsönzés azonosítóját: "))

                torolt_kolcsonzes, hiba = kolcsonzes_manager.kolcsonzes_lemondasa(kolcsonzes_id)

                if not torolt_kolcsonzes:
                    print(f"Hiba a kölcsönzés lemondásakor: {hiba}")
                else:
                    print(f"A következő kölcsönzés sikeresen lemondva: {torolt_kolcsonzes}")
            except ValueError:
                print("Érvénytelen kölcsönzés azonosító!")

        elif valasztas == "4":
            print("\nÖsszes aktív kölcsönzés:")
            kolcsonzesek = kolcsonzes_manager.osszes_kolcsonzes_listazasa()

            if not kolcsonzesek:
                print("Nincs aktív kölcsönzés a rendszerben.")
            else:
                for kolcsonzes in kolcsonzesek:
                    print(kolcsonzes)

        else:
            print("Érvénytelen választás! Kérem, válasszon 0 és 4 között.")


if __name__ == "__main__":
    main()