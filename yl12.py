# yl12
# Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
# Väljasta listi esimene väärtus
# Lisa listi lõppu uus puuvili
# Väljasta listi viimane väärtus
# Muuda ühe elemendi väärtust ja väljasta kogu list
# Kontrolli kas väärtus (näiteks õun) eksisteerib listis
# Väljasta listi pikkus
# Eemalda listist element ja väljasta kogu list
# Muuda listi järjekord vastupidiseks
# Sorteeri list ja väljasta
# (jada, list, listi element, listi meetodid)
# https://www.w3schools.com/python/python_lists.asp


list = ["kirss", "banaan", "pirn"]
print(list)
print(list[0])
list.append("õun")
print(list[-1])
list[1] = "apelsin"
print(list)
list[3] = "ploom"
print(list)
size = len(list)
# print(size)
list.remove("õun")
print(size)
check = input("kas on listis? ")
if check in list:
    print("on listis")
else:
    print("ei ole listis")
list.reverse
print(list)
print(sorted(list))