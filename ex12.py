#Exercici 12
def main():
    paraula = input("Introdueix una paraula: ")
    text    = (paraula + " ") * 1000
    print(text.rstrip())

if __name__ == "__main__":
    main()