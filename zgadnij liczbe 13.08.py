misteriousNumber = 16
guessNumber = 0
while guessNumber != misteriousNumber :
    guessNumber = int(input("Guess number: "))

    if (misteriousNumber < guessNumber) :
        print ("That's to much ")
    elif (misteriousNumber > guessNumber) :
        print ("Cmon add some more")
    else:
        print("Congratulations!")    
