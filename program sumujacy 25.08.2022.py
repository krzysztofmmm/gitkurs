wynik = 0
i = 0
while  i < 4:
    x = int(input("podaj liczbe:"))
    wynik += x
    i += 1

print("wynik dodawania to:", wynik)

"""
Napisz program, który policzy sumę wszystkich liczb od 1 do podanej liczby

Dla np. 5
1+2+3+4+5
zwróci
15

range(6)
1,2,3,4,5
(1 + 5) / 2 * 5 = 15

"""
def sumuj_do(liczba):
    suma = 0
    
    for liczba in range(1,liczba+1):
        suma = suma + liczba
        
    return suma

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1,liczba+1)])

def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1,liczba+1)})

def sumuj_do4(liczba):
    return sum((liczba for liczba in range(1,liczba+1)))

def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba
    

print(sumuj_do(25))
print(sumuj_do2(25))
print(sumuj_do3(25))
print(sumuj_do4(25))
print(sumuj_do5(25))
