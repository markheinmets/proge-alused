# yl11
# Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# Eemalda selle sisendi algusest ja lõpust tühikud.
# String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja 
# et sümbolite arv on paarituarvuline.
# Väljasta selle stringi kolm keskmist sümbolit.
# (stringi meetodid, list)



""" a = input("Sisesta vähemalt 7 kohaline paarituarvuline sisend: ").strip()


if len(a) >= 7 and len(a) % 2 != 0 :
    print(a)
    x = len(a)
    y = x // 2
    print("Stringi kolm keskmist elementi on:" ,a[y-1]+a[y]+a[y+1])
else: 
    print("Error") """

# Küsime kasutajalt sisendit
x = input("Sisesta string: ")

# Eemaldame alguse ja lõpu tühikud
stripped = x.strip()

# Kontrollime, kas tingimused on täidetud
if len(stripped) >= 7 and len(stripped) % 2 == 1:
    # Leiame keskmise indeksi
    middle = len(stripped) // 2

    # Väljastame kolm keskmist sümbolit
    result = stripped[middle - 1 : middle + 2]
    print("Kolm keskmist sümbolit:", result)
else:
    print("Sisestatud string ei vasta nõuetele.")



