# yl8
# Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number.
# Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.

n = int(input("potsitiivne täisarv: "))
if (n % 400 == 0) or (n % 4 == 0) and (n != 100) :
    print(n, "liigaasta")
else:
    print(n, "lihtaasta")