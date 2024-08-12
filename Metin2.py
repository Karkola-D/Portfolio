
from collections import Counter

Overwatch_Spieler_Ingame_Item = {
"yang": 100000,
"DIVA": 16

}

Ingame_Shop = {
    "yang": 1000,
    "DIVA": 1
}

neue_Ingame = Counter(Overwatch_Spieler_Ingame_Item)
neue_Ingame.subtract(Ingame_Shop)
print(neue_Ingame)
for item, anzahl in neue_Ingame.items():
    print(f'{item}:{anzahl}:')
