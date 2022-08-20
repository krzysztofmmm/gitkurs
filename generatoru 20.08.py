import sys

evenNumbersGenerator = (element
                        for element in range(101)
                        if (element **2 )
                        )
print(sum(evenNumbersGenerator))
print (evenNumbersGenerator)