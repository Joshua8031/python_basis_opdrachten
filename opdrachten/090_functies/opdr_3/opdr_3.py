# Opdracht 1 functies
# Naam student:
# Groep:


def kubus_vol(m):
    volume = zijde ** 3
    return volume

zijde = 5
volume = kubus_vol(zijde)

print(f"Het volume van de kubus met zijde {zijde} is {volume}")

import math

def bol_vol(r):
    volume = (4/3) * math.pi * r ** 3
    return volume

radius = 4
volume = bol_vol(radius)

print(f"Het volume van de bol met straal {radius} is {volume}")

print(kubus_vol(5))
print(bol_vol(4))

