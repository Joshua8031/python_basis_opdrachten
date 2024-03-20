# Opdracht 1 input function
# Naam student: joshua
# Groep: 4ITX1

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

a = int(input("Geef de lengte van de eerste zijde"))
b = int(input("Geef de lengte van de tweede zijde"))

c = a**2 + b**2

c = round(math.sqrt(c),2)
print(c)



