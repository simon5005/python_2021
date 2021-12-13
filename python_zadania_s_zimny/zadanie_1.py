#! /usr/bin/env python   



#print ("Hello World!")

def hi_function():
    print("Hello")



def name_date():
    imie,nazwisko,data_urodzenia = input("Wpisz imie nazwisko i date urodzenia:\n").split(" ",3)
    print(data_urodzenia)



def keylock():
    print("Wpisz pin: ")
    passwd = int(input())
    print("Podaj ponownie pin: ")

    temp = int(input())
    if (temp != passwd):
        print("Pin niepoprawny")
    else:
        print("Pin poprawny")


if __name__ == "__main__":
    #hi_function()
    name_date()
    #keylock()