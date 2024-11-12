#Exercici 10
def main():
    try:
        num1 = float(input("Introdueix el 1er operand: "))
        num2 = float(input("Introdueix el 2on operand: "))

        tupla = (num1, num2)

        print(f"{tupla[0]} + {tupla[1]}  = {tupla[0]+tupla[1]:.2f}")
        print(f"{tupla[0]} - {tupla[1]}  = {tupla[0]-tupla[1]:.2f}")
        print(f"{tupla[0]} * {tupla[1]}  = {tupla[0]*tupla[1]:.2f}")
        print(f"{tupla[0]} / {tupla[1]}  = {tupla[0]/tupla[1]:.2f}")
        print(f"{tupla[0]} // {tupla[1]} = {tupla[0]//tupla[1]:.0f}")
        print(f"{tupla[0]} % {tupla[1]}  = {tupla[0]%tupla[1]:.0f}") 
    except ValueError:
        print("Els operands han de ser números.")
        exit(1)
    except ZeroDivisionError:
        print("No es pot dividir per zero.")
        exit(2)

if __name__ == "__main__":
    main()