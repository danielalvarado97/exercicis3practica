#Exercici 17
def main():
    try:
        nota = float(input("Introdueix la teva qualificació: "))
        if nota < 0 or nota > 10: raise ValueError
        match(nota):
            case x if x < 5     : print("Suspès")
            case x if x < 6     : print("Aprovat")
            case x if x < 7     : print("Bé")
            case x if x < 9     : print("Notable")
            case x if x <= 10   : print("Excel·lent")
    except ValueError:
        print("La qualificació ha de ser un valor numèric entre 0 i 10")

if __name__ == "__main__":
    main()