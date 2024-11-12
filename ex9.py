#Exercici 9
def main():
    try:
        capitalIni = float(input("Introdueix el capital inicial: "))
        taxaIntAnu = float(input("Introdueix la taxa d'interès anual: "))
        nombreAnys = int(input("Introdueix el nombre d'anys: "))

        capitalFinal = capitalIni * (1 + taxaIntAnu/100)**nombreAnys
        print(f"El capital final és de {capitalFinal:.2f}€")
    except ValueError:
        print("Error: Introdueix un valor numèric acceptable")

if __name__ == "__main__":
    main()