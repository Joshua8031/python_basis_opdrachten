# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

enquete1 = input("Wat vind je van de huidige regering?")
enquete2 = input("Wat vind je van de Python-lessen tot nu toe?")
enquete3 = input("Wat vind jij de mooiste stad van Nederland?")


with open("enquate_resultaten.txt", "w") as text:
       text.write("resultaten enquate:\n")
       text.write("1. Wat vind je van de huidige regering?" + enquete1 + "\n")
       text.write("2. Wat vind je van de Python-lessen tot nu toe?" + enquete2 + "\n")
       text.write("3. Wat vind jij de mooiste stad van Nederland?" + enquete3 + "\n")
        
print("prima enquate oke>")

