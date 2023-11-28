import secrets
import string

#print(secrets.choice("ab"))

chars = string.digits + string.ascii_letters + string.punctuation
print(len(chars)) # Gibt die länge des chars an. "94 Buchstaben enthalten"                   Entropie: 6,555 , Min: 100Bit vorgabe vom BND.
print(100/6.555) # print(100/6.555) = 16 // Advanced Encryption Standard(AES) print(256/6.555) = 40   6.555 Entropie ist im jeden Buchstaben 
print("Deine neues Passwort:","".join(secrets.choice(chars) for _ in range(40)))