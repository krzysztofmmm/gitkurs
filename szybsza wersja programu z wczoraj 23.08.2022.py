import menu

from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figure', 'Prostokat Kwadrat Trojkat Trapez Kolo')

while(True):
    choice = int(input("""Select the figure whose field you want to calculate: 
    1. Rectangle
    2. Square
    3. Triangle
    4. Trapezium
    5. Cirlce
    6. End up program               
    """))

    if (choice == Menu_Figury.Prostokat):
        a = float(input("Specify the lenght side of the rectangle: "))
        b = float(input("Specify the lenght second side of the rectangle: "))
        print("Rectangle field is:", menu.pole_prostokata(a, b))
        
    elif (choice == Menu_Figury.Kwadrat):
        a = float(input("Specify the lenght side of the square: "))
        print("Squere field is:", menu.pole_kwadratu(a,))
        
    elif (choice == Menu_Figury.Trojkat):
        a = float(input("Specify the side length of the triangle: "))
        h = float(input("Specify triangle height: "))
        print("Triangle field is:", menu.pole_trojkata(a, h))
        
    elif (choice == Menu_Figury.Trapez):
        a = float(input("Specify the length of the trapezoid base: "))
        b = float(input("Specify the length of the second trapezoid base: "))
        h = float(input("Specify trapezoidal height: "))
        print("Trapezoid field is:", menu.pole_trapezu(a, b, h))
        
    elif (choice == Menu_Figury.Kolo):
        r = float(input("Specify the length of the radius:"))
        print("Circle field is:", menu.pole_kola(r))
        
    elif (choice == 6):
        print("Program operation is finished")
        break
    
    else:
        print("You can only select from the specified numbers")