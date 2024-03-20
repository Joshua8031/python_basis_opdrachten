# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)
aantal_pogingen = 0

print("welkom bij 'Raad het nummertje'")
print("Ik heb een getal tussen 1 en 100. Raad welk getal het is")

while True:
    poging = int(input("Voer een getal in:" ))
    aantal_pogingen += 1

    if poging < geheim_getal:
        print("Hoger swa")
    elif poging > geheim_getal:
        print("Lager swa")
    else:
        print(f"Prima oke! {aantal_pogingen} pogingen") 
        break
    