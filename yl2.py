# yl2
# Kirjuta programm, mis küsib kasutajalt raadiuse ja arvutab ringi pindala ja ümbermõõdu. (math.pi)


import math

radius = float (input("Sisesta raadius: "))
area = math.pi * radius ** 2
print("Pindala:", area,)

perimetre = 2 * math.pi * radius 
print("Ümbermööt:", perimetre)