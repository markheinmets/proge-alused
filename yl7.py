# yl7
# Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud
# täisarv on paarisarv või mitte. (paarisarvu mõiste - odd/even)

n = int(input("sisesta number: "))
if  (n % 2) == 0:
   print("{0} on paarisarv".format(n))
else:
   print("{0} on paarituarv".format(n))

if n % 2 == 1:
    print(n,"on paaritu arv")
else:
   print(n,"on paarisarv")