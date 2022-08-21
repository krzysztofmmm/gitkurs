names = {"krzysiek", "anes", "janbarbar", "kasia"}
number = [1, 2, 3, 4, 5, 6, 7, 8]
celcius = {'tl': -20, 't2' : -15, 't3' : -22, 't4' : -13}


namesLenght = {
    name: len(name)
    for name in names
    if name.startswith("A")
}

mulipliedNumbers = {
   number : number*number
    for number in number 
}
#poteguj od2-6  potegi

fahrenhait = {
    key: celcius * 1.8 + 32
    for key, celcius in celcius.items()
}
