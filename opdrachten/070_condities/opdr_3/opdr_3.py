# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...
def toegangprijs(leeftijd):
    if 0 <= leeftijd <= 2:
        groep = "baby's"
        korting = 100
        prijs = 12.50
    elif 3 <= leeftijd <= 18:
        groep = "kinderen"
        korting = 50
        prijs = 12.50
    elif 19 <= leeftijd <= 64:
        groep = "volwassenen"
        korting = 0
        prijs = 12.50
    elif 65 <= leeftijd <= 150:
        groep = "ouderen"
        korting = 30
        prijs = 12.50 
    
    korting_bedrag = prijs * (korting / 100)
    betalen = prijs - korting_bedrag

    return groep, korting, betalen

leeftijd = int(input("Leeftijd"))
groep, korting, betalen = toegangprijs(leeftijd)

print("U behoort tot de groep", groep)
print("U krijgt", korting, "% korting")
print("U betaalt daarom", betalen)

