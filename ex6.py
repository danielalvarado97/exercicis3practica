# Demanem a l'usuari dos números
a = int(input("Introdueix el primer número (A): "))
b = int(input("Introdueix el segon número (B): "))

# Mostrem els valors originals
print(f"Abans de l'intercanvi: A = {a}, B = {b}")

# Intercanviem els valors
temp = a  # Guardem el valor de 'a' en una variable temporal
a = b     # Assignem el valor de 'b' a 'a'
b = temp  # Assignem el valor temporal a 'b'

# Mostrem els nous valors
print(f"Després de l'intercanvi: A = {a}, B = {b}")