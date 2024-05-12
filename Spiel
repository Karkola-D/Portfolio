import random

print("Willkommen zu Schere Stein Papier!")

möglichkeiten = ["Schere", "Stein", "Papier"]

weiterspielen = True


while weiterspielen:

    computer_geste = random.choice(möglichkeiten)
    
    spieler_geste = None
    while spieler_geste not in möglichkeiten:
        print("Verfügbare Gesten: ", *möglichkeiten)
        spieler_geste = input("Bitte wählen Sie eine Geste aus: ")
        
    print(f"Sie haben {spieler_geste} gewählt, der Computer {computer_geste}: ", end="")
    if spieler_geste == computer_geste:
        print("Unentschieden!")
    elif (
        (spieler_geste == "Schere" and computer_geste == "Papier")
        or (spieler_geste == "Stein" and computer_geste == "Schere")
        or (spieler_geste == "Papier" and computer_geste == "Stein")
    ):
        print("Sie haben gewonnen!")
        
    else:
        print("Leider verloren")
     
    if input("Weiterspielen (j/n)? ") == "n":
        weiterspielen = False
