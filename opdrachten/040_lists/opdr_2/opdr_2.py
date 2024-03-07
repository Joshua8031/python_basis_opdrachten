# Opdracht 2 lists
# Naam student: joshua
# Groep: 4ITX1


rivier_info = {
    "Rijn": ["Nederland", "Duitsland", "Frankrijk"],
    "Maas": ["Nederland", "België", "Duitsland"],
    "Nijl": ["Egypte", "Soedan", "Oeganda"]
}

baraaaa = "Rijn"
sisi = "Maas"
lamar = "Nijl"
rivier = list(rivier_info.keys())

# print de naam van de eerste rivier
print(baraaaa)
print("De rivier", rivier[0].capitalize(), "stroomt door", rivier_info[rivier[0]][1].capitalize())

# print de naam van de tweede rivier
print(sisi)
print("De rivier", rivier[0].capitalize(), "stroomt door", rivier_info[rivier[1]][1].capitalize())

# print de naam van de derde rivier
print(lamar)
print("De rivier", rivier[0].capitalize(), "stroomt door", rivier_info[rivier[2]][2].capitalize())