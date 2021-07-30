'''
Random Zeichen, z.B. Passwörter
'''
import secrets
import string

# Zahlen, Zeichen, Punkte
chars = string.digits + string.ascii_letters + string.punctuation
print(len(chars)) # Entropie: 6.555, Min 100Bit
print(256/6.555)

# secrets wählt random-mäßig 40 Zeichen aus den chars, die definiert wurden
print(''.join(secrets.choice(chars) for _ in range(40)))
