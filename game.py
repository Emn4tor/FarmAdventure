import random
import time

# Verfügbare Pflanzen und Grundstücke ab bestimmten Leveln
freigeschaltete_pflanzen = {
    "Weizen": 1,
    "Karotten": 2,
    "Tomaten": 3,
    "Gurken": 4,
    "Apfelbaum": 5,
    "Kürbis": 6,
    "Melonen": 7,
    "Kokosnuss": 8
}
freigeschaltete_grundstuecke = {"Feld": 1, "Scheune": 2}

# XP-Grenzen für Level
xp_grenzen = {1: 50, 2: 100, 3: 100, 4: 150, 5: 200, 6: 200, 7: 250, 8: 250}

class Spieler:
    def __init__(self, name):
        self.name = name
        self.geld = 100
        self.inventar = {"Weizen": 0, "Karotten": 0, "Tomaten": 0, "Gurken": 0, "Apfelbaum": 0, "Kürbis": 0, "Melonen": 0, "Kokosnuss": 0}
        self.xp = 0
        self.level = 1
        self.max_inventar_groesse = 5
        self.felder = 1
        self.scheune = 1
        self.schlaf_cooldown = 300  # 5 Minuten in Sekunden

    def zeige_status(self):
        print(f"{self.name} - Geld: {self.geld} - Felder: {self.felder} - Scheune: {self.scheune} - Inventar: {self.inventar} - Level: {self.level} - XP: {self.xp}")
        print("\nVerfügbare Pflanzen:")
        for pflanze, freischalt_level in freigeschaltete_pflanzen.items():
            if freischalt_level <= self.level:
                print(f"{pflanze}: Freischaltung (Level {freischalt_level})")

        print("\nVerfügbare Grundstücke:")
        for objekt in ['Feld', 'Scheune']:
            preis = self.berechne_preis(objekt)
            if objekt in freigeschaltete_grundstuecke and preis <= self.geld:
                print(f"{objekt} kaufen - {preis} Gold")

    def laden(self):
        print("Willkommen im Laden! Was möchtest du kaufen?")
        print("1. Samen kaufen")
        print("2. Grundstücke kaufen")
        print("3. Zurück zum Hauptmenü")

        auswahl = input("Deine Auswahl: ")

        if auswahl == "1":
            self.kaufe_samen()
        elif auswahl == "2":
            self.grundstuecke_laden()
        elif auswahl == "3":
            pass
        else:
            print("Ungültige Auswahl. Versuche es erneut.")

    def grundstuecke_laden(self):
        print("Willkommen im Bereich für Grundstücke! Was möchtest du kaufen?")
        print(f"4. Feld kaufen - {self.berechne_preis('Feld')} Gold")
        print(f"5. Scheune kaufen - {self.berechne_preis('Scheune')} Gold")
        print("6. Zurück zum Laden")

        auswahl = input("Deine Auswahl: ")

        if auswahl == "4":
            self.kaufe_feld()
        elif auswahl == "5":
            self.kaufe_scheune()
        elif auswahl == "6":
            pass
        else:
            print("Ungültige Auswahl. Versuche es erneut.")

    def kaufe_feld(self):
        preis = self.berechne_preis('Feld')
        if self.geld >= preis:
            self.geld -= preis
            self.felder += 1
            self.max_inventar_groesse += 5
            print(f"Du hast ein Feld für {preis} Gold gekauft. Jetzt hast du {self.felder} Felder!")
        else:
            print("Nicht genug Geld!")

    def kaufe_scheune(self):
        preis = self.berechne_preis('Scheune')
        if self.geld >= preis:
            self.geld -= preis
            self.scheune += 1
            self.max_inventar_groesse += 5
            print(f"Du hast eine Scheune für {preis} Gold gekauft. Deine Inventargröße wurde auf {self.max_inventar_groesse} erhöht!")
        else:
            print("Nicht genug Geld!")

    def kaufe_samen(self):
        print("Welche Pflanze möchtest du kaufen?")
        for pflanze, preis in preise.items():
            print(f"{pflanze}: {preis} Gold")
        
        auswahl = input("Deine Auswahl: ")
        menge = int(input(f"Wie viele {auswahl} möchtest du kaufen? ")) if auswahl in preise else 0
        
        if auswahl in preise and self.geld >= preise[auswahl] * menge:
            self.geld -= preise[auswahl] * menge
            self.inventar[auswahl] += menge
            print(f"Du hast {menge} {auswahl} gekauft!")
        else:
            print("Ungültige Auswahl oder nicht genug Geld!")

    def pflanze_aussaen(self):
        print("Du möchtest Pflanzen anbauen. Welche Pflanze möchtest du aussäen?")
        for pflanze in preise:
            print(f"{pflanze}: Kostenlos")
        auswahl = input("Deine Auswahl: ")

        if auswahl in preise:
            menge = int(input(f"Wie viele {auswahl} möchtest du aussäen? "))
            if menge <= self.felder:
                self.inventar[auswahl] -= menge
                self.felder -= menge
                self.ernte_pflanzen(auswahl, menge)
                print(f"Du hast {menge} Felder mit {auswahl} bepflanzt!")
            else:
                print("Nicht genug Pflanzen oder Felder!")
        else:
            print("Ungültige Auswahl.")

    def ernte_pflanzen(self, pflanze, menge):
        wachstumszeit = 30  # Zeit in Sekunden, die die Pflanze zum Wachsen benötigt
        print(f"Die {pflanze}-Pflanzen wachsen. Bitte warte {wachstumszeit} Sekunden.")
        time.sleep(wachstumszeit)

        ertrag = random.randint(1, 10) * menge
        self.inventar[pflanze] += ertrag
        self.xp += xp_werte[pflanze]
        print(f"Du hast {ertrag} {pflanze} geerntet und {xp_werte[pflanze]} XP erhalten!")

        if self.xp >= xp_grenzen[self.level]:
            self.level_up()

    def level_up(self):
        self.level += 1
        print(f"Gratuliere! Du bist jetzt Level {self.level}!")

    def starte_kampf(self):
        if time.time() - self.schlaf_cooldown < 300:
            print("Du bist zu müde für einen Nachtangriff. Erhole dich und versuche es später erneut.")
            return

        print("Willkommen zum Nachtangriff! Löse 10 einfache + und - Aufgaben in 10 Sekunden.")
        aufgaben_richtig = 0

        for _ in range(10):
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            operator = random.choice(['+', '-'])
            frage = f"Frage: {num1} {operator} {num2} = "
            antwort = int(input(frage))

            if operator == '+' and antwort == num1 + num2:
                aufgaben_richtig += 1
            elif operator == '-' and antwort == num1 - num2:
                aufgaben_richtig += 1

        if aufgaben_richtig == 10:
            belohnung = self.berechne_nachtangriff_belohnung()
            print(f"Herzlichen Glückwunsch! Du hast den Nachtangriff überstanden und bekommst {belohnung} Münzen sowie 1 Leben.")
            self.geld += belohnung
            self.schlaf_cooldown = time.time()
        else:
            print("Du hast einen Fehler gemacht und den Nachtangriff nicht überstanden. Du verlierst 1 Leben.")
            # Implementiere die Logik für den Verlust eines Lebens hier

    def berechne_nachtangriff_belohnung(self):
        if self.felder <= 2:
            return 50
        elif 3 <= self.felder <= 7:
            return 90
        elif 8 <= self.felder <= 15:
            return 120
        else:
            return 150

    def berechne_preis(self, objekt):
        preis = {
            'Feld': 20 * self.felder,
            'Scheune': 50 * self.scheune
        }
        return int(preis[objekt] * 1.05)

# Preise für Pflanzen
preise = {"Weizen": 5, "Karotten": 8, "Tomaten": 10, "Gurken": 50, "Apfelbaum": 100, "Kürbis": 125, "Melonen": 150, "Kokosnuss": 175}

# XP-Werte für Pflanzen
xp_werte = {"Weizen": 5, "Karotten": 6, "Tomaten": 8, "Gurken": 15, "Apfelbaum": 19, "Kürbis": 22, "Melonen": 25, "Kokosnuss": 27}

# XP-Grenzen für Level
xp_grenzen = {1: 50, 2: 100, 3: 100, 4: 150, 5: 200, 6: 200, 7: 250}

# Hauptprogramm
spielername = input("Wie möchtest du genannt werden? ")
spieler = Spieler(spielername)

while True:
    spieler.zeige_status()
    print("\n1. Laden\n2. Pflanze aussäen\n3. Starte Nachtangriff\n4. Beende das Spiel")
    auswahl = input("Deine Auswahl: ")

    if auswahl == "1":
        spieler.laden()
    elif auswahl == "2":
        spieler.pflanze_aussaen()
    elif auswahl == "3":
        spieler.starte_kampf()
    elif auswahl == "4":
        print("Vielen Dank fürs Spielen! Auf Wiedersehen.")
        break
    else:
        print("Ungültige Auswahl. Versuche es erneut.")
