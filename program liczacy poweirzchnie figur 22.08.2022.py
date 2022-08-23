import math

while True:
    
    print("1: kwadrat ")
    print("2: prostokąt")
    print("3: kolo")
    print("4: trójkąt")
    print("5: trapez")
    print("6: zakończ")
 
    wybor = input("Pole jakiej figury chcesz obliczyc?: ")

    if wybor == "1":
        kbok = int(input("Podaj długość boku kwadratu: "))
        def kwadrat(kbok):
            return kbok**2
        print("Pole kwadratu wynosi:", kwadrat(kbok))
        
    elif wybor == "2":
        pbok1 = int(input("Podaj długość pierwszego boku prostokąta: "))
        pbok2 = int(input("Podaj długość drugiego boku prostokąta: "))
        def prostokat(pbok1, pbok2):
            return pbok1 * pbok2
        print("Pole prostokąta wynosi:", prostokat(pbok1, pbok2))
    
    elif wybor == "3":
        r = int(input("Podaj promien kola: "))
        def pole_kola(r):
            return math.pi * r ** 2
        print("Pole kola wynosi:", pole_kola(r))
    
    elif wybor == "4":
        a = int(input("Podaj dlugosc boku trojkata: "))
        h = int(input("Podaj wysokosc trojkata: "))
        def pole_trojkata(a, h):
            return (0.5 * a) * h
        print("Pole trojkata wynosi:", pole_trojkata(a, h))
        
    elif wybor == "5":
        a = int(input("Podaj dlugosc jednej z podstaw trapezu: "))  
        b = int(input("Podaj dlugosc drugiej z podstaw trapezu: "))   
        h = int(input("Podaj wysokosc trapezu: "))  
        def pole_trapezu(a, b, h):
            return (a + b) / 2 * h
        print("Pole trapezu wynosi:", pole_trapezu(a, b, h))
    
    elif wybor == "6":
       print("Działanie programu zakonczone.")
       break
    else:
        print("Wybrales niewłasciwa wartosc. Wybierz miedzy 1-6")  
