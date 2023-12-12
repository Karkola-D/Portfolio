import time

class Lampe:
    def __init__(self):
        self.zustand = "rot"
        self.ampelzeit = 10

    def schalte_an(self):
        print("Die Lampe wird geschaltet.")
        self.zustand = "grün"

    def schalte_aus(self):
        print("Die Lampe wird ausgeschaltet.")
        self.zustand = "rot"

    def ampelzeit_umschalten(self):
        if self.zustand == "rot":
            self.ampelzeit = 10
        else:
            self.ampelzeit = 5

    def __str__(self):
        return f"Lampe: Zustand={self.zustand}, Ampelzeit={self.ampelzeit}"


def main():
    # Lampe erstellen
    lampe = Lampe()

    # Lampe anschalten
    lampe.schalte_an()

    # 10 Sekunden warten
    time.sleep(5)

    # Lampe ausschalten
    lampe.schalte_aus()

    # 5 Sekunden warten
    time.sleep(5)

    # Ampelzeit umschalten
    lampe.ampelzeit_umschalten()

    # Lampe anschalten
    lampe.schalte_an()

    print(lampe)


if __name__ == "__main__":
    main()