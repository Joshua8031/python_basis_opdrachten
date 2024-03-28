# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(afile, atext):
    fo = open(afile, "w")
    fo.write(atext)
    fo.close()

write_to_file("test.txt","wagwan mensen")

write_to_file("test1.txt","yo")