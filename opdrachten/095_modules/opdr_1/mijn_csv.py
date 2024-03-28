


import csv

def lees_csv_bestand(jj):
    data = []
    with open(jj, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.appennd(row)
    return data

def schrijf_csv_bestand(sisi, data):
    with open(sisi, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)