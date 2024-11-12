import math

# Demanem a l'usuari que introdueixi el radi del cercle
radi = float(input("Introdueix el radi del cercle: "))

# Calculem l'àrea del cercle
area = math.pi * (radi ** 2)

# Calculem el perímetre del cercle
perimetre = 2 * math.pi * radi

# Imprimim els resultats amb 2 decimals
print(f"Àrea: {area:.2f}")
print(f"Perímetre: {perimetre:.2f}")