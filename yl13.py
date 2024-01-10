# yl13
# Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
# Koosta list, mis koosneb kolmest loomast.
# Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
# Väljasta see lemmikloomade list.
# Väljasta listi viimase elemendi viimane täht.
# (sõne kui list, mitmemõõtmeline list - multi dimensional)


animal = input("Mis on sinu lemmikloom? ")
print(animal[0])
mylist = ["koer", "kass", "ahv"]
print(mylist)
mylist.append(animal)
print(mylist)
print(mylist[-1][-2:])

