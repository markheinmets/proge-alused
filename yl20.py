#  Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
# 8 x 0 = 0
# 	8 x 1 = 8
# 	8 x 2 = 16
# 	…
# 	8 x 12 = 96
# Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse


# Küsime kasutajalt arvu x
x = int(input("Sisesta arv x: "))

# Väljund pealkiri
print(f"{x} korrutustabel:")

# Loome tsükli arvudega 0 kuni 12
for i in range(13):
    # Korrutame x-i ja i
    result = x * i
    # Väljastame vormindatud väljundi
    print(f"\t{x} x {i} = {result}")

