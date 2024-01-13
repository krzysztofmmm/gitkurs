wybor = input ("* - mnozenie, / - dzielenie, + - dodawanie, - - odejmowanie, ** - potegowanie:")

a = int(input("pierwsza liczba:"))
b = int(input("druga liczba:"))

if (wybor == '*') :
    print(a * b)
elif (wybor == '/') :
    if (a==0 or b==0):
        print("nie dziel przez zero")
    else:
        print(a / b )
elif (wybor == '+') :
    print (a + b)
elif (wybor == '-') :
    print (a - b)
elif (wybor == '**') :
    print (a**b)   
else:
    print ("zly wybor")