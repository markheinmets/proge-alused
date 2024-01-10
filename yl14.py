# yl14
# Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext”
# (ext - extension - faili laiend) ja prindib välja laiendi (“ext”). (str.split)


filename = input("kirjuta faili nimi: ")
print("faili laiendiks on", filename.split(".")[-1])