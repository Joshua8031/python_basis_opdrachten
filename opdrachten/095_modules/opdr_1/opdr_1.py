# Opdracht 1 functies
# Naam student:
# Group:

programma
|-- opdr_1.py
|-- my_modules
    |-- __init__.py
    |-- csv.py


from my_modules import mijn_csv

data = [
    ['Naam', 'Leeftijd', 'Stad'],
    ['Yaya', '50', 'London'],
    ['Bobby', '45', 'shmurda'],
    ['Bombo', '20', 'clat'],
]


mijn_csv.schrijf_csv_bestand('data.csv', data)
print("CSV-bestand geschreven")

gelezen_data = mijn_csv.lees_csv_bestand('data.csv')
print("Gelezen data uit CSV-bestand:")
print(gelezen_data)
