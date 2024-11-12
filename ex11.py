#Exercici 11
def main():
    try:
        num1 = float(input("Introdueix el 1er Número: "))
        num2 = float(input("Introdueix el 2on Número: "))
        if num1 == num2: print("Els números són iguals")
        elif num1 > num2: print("El 1er número és més gran")
        else: print("El 2on número és més gran")
    except ValueError:
        print("Error: Introdueix un número vàlid") 
if __name__ == "__main__":
    main()