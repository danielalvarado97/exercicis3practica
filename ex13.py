#Exercici 13
def main():
    ADMIN_USER = "admin"
    ADMIN_PASS = "admin"
    
    username = input("Introdueix l'usuari: ")
    password = input("Introdueix la passw: ")

    if(username==ADMIN_USER and password==ADMIN_PASS):
        print("Accés Garantit")
    else:
        print("Accés Denegat")

if __name__ == "__main__":
    main()