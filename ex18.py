#Exercici 18
llista = [] #Això és una llista buida
print(f"Llista: {llista}")

for i in range(1,6):
    element = input(f"Introdueix un element ({i}): ")
    llista.append(element) #Afegim element a la llista
    print(f"Llista: {llista}")

print(f"Primer Element {llista[0]}")
print(f"Darrer Element {llista[-1]}")