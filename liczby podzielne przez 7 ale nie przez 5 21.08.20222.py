#znajdz liczby od 2-470 wlacznie kotre sa podzielne przez 7 ale nie przez 5
#generator lub wyrazenie listowe lub wyrazenie zbioru lub wyrazenie slownikowe
#zastanow sie czy odpowiedz na to pytanie zawsze jest taka sama

numbers = {
     number
     for number in range (2, 471)
     if (number % 7 == 0)
     if (number % 5 !=0)
     }
for number in numbers :
     print (number)
     
