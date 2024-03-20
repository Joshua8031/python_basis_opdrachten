# Opdracht 2 berekeningen
# Naam student: Joshua
# Groep: 4ITX1

# Hier komt je code...

gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
print(gasten)

del gasten[gasten.index('Marie')]
print(gasten)

plekKees = gasten.index('Kees')

gasten.insert(plekKees + 1, 'George')
print(gasten)