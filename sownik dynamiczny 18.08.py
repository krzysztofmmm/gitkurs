definitions = {}

while (True) :
    print ("1: Add definitions")
    print ("2: Search definitions")
    print ("3: Delate definitions")
    print ("4: Close dictionary")

    choice = input ("What u want to do? ")
    
    if (choice == "1") :
        key = input("Write a key (word) to define: ")
        definition = input("Write meaning of this word: ")
        definitions[key] = definition
        print("Definition added successfully")
    elif (choice == "2") :
        key = input ("What are u looking for:")
        if key in definitions :
            print(definitions[key])
        else:
            print("theres no definiions called ", key)
    elif (choice == '3') :
        key = input ("which definition you want to delate:")
        if key in definitions :
            del(definitions[key])
            print (key, "dissapear")
        else:
            print("not found definition called", key)
    elif (choice == "4") :
        print ("the end is here")
        break
    else:
        print("U can only choose from 1-4")
