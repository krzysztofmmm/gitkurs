names = {"arek", "bartek", "marcin", "blazej", "elzbieta"}

wrongLitters = ['b']

names = {
    name.capitalize() 
    for name in names
    if name[0] != "b" and name[0] != "B"
    }
print(names)
