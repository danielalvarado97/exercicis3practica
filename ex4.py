# Demanem a l'usuari que introdueixi la base del rectangle
base = float(input("Introdueix la base del rectangle: "))

# Demanem a l'usuari que introdueixi l'altura del rectangle
altura = float(input("Introdueix l'altura del rectangle: "))

# Calculem l'àrea del rectangle
area = base * altura

# Calculem el perímetre del rectangle
perimetre = 2 * (base + altura)

# Imprimim els resultats amb un decimal 1f
print(f"Àrea: {area:.1f}")
print(f"Perímetre: {perimetre:.1f}")