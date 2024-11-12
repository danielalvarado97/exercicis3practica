#Exercici 16
def main():
    try:
        year = int(input("Enter a year number: "))
        tras = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
        print("Leap year") if tras else print("Not a leap year")
    except ValueError:
        print("Oh my godness! The year is not an int!")

if __name__ == "__main__":
    main()