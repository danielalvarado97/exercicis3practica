#Exercici 15
def main():
    try:
        mes = int(input("Introdueix un número de mes: "))
        match(mes):
            case 1|3|5|7|8|10|12: print("El mes té 31 dies")
            case 4|6|9|11       : print("El mes té 30 dies")
            case 2              : print("El mes té 28 o 29 dies en funció de l'any")
            case _              : raise ValueError
    except ValueError:
        print("El mes hauria de ser un valor numèric sencer entre 1 i 12")

if __name__ == "__main__":
    main()