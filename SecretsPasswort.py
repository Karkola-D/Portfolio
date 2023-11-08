import secrets
import string

"""print(secrets.choice("ab"))"""

chars = string.digits + string.ascii_letters + string.punctuation
print(len(chars)) # Entropie: 6,555 , Min: 100Bit
print(100/6.555) # 16
print("".join(secrets.choice(chars) for _ in range(40)))