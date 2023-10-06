# yl6
# Kirjuta programm, mis leiab kolmest kasutaja 
# poolt sisestatud arvust maksimumi
# (ära kasuta max funktsiooni). 
# (loogikatehted - logic operators)

a = input("sisesta a: ")
b = input("sisesta b: ")
c = input("sisesta b: ")

if a > b and a > c: 
    print("maksimum arv: ", a)
elif b > c:
    print("maksimum arv: ", b)
else:
    print("maksimum arv: ", c)
