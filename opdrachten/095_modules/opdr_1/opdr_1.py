# Opdracht 1 functies
# Naam student:
# Group:



from my_modules import mijn_csv

persons = []
for line in open("test.csv", 'rt'):
    lst = mijn_csv.sanitize(line)
    person = mijn_csv.create_person(lst)
    person = mijn_csv.add_fullname(person)
    persons.append(person)

mijn_csv.print_persons(persons)
