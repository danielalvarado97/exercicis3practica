#Exercici 14
def main():
    try:
        minuts = int(input("Introdueix el nombre de minuts: "))
        horaT = minuts // 60
        minsT = minuts % 60
        print(f"Has indicat {horaT} hores i {minsT} minuts.")
    except ValueError:
        print("Només s'admeten valors sencers pels minuts")

if __name__ == "__main__":
    main()