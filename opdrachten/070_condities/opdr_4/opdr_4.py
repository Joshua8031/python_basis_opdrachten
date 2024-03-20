# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = ...

def kies_topping():
    beschikbare_toppings = ", ".join([topping[0] for topping in toppings])
    print(f"Beschikbare toppings: {beschikbare_toppings}")

    while True:
        keuze = input("Kies een topping uit de lijst") 
        if keuze.lower() == 'stop':
            return None
        else:
            gevonden = False
            for topping in toppings:
                if keuze.lower() == topping[0].lower():
                    gevonden = True
                    return topping
            if not gevonden:
                print("Uw keuze zit niet in ons assortiment.")

gekozen_topping = kies_topping()

if gekozen_topping is not None:
    topping_naam, topping_prijs = gekozen_topping
    print(f"Je hebt gekozen voor {topping_naam} voor een prijs van €{topping_prijs}.")
