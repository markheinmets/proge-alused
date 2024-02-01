# Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv. 

# Etteantud tekst
text = "Tere, see on näide tekstist, mille hulgas on täishäälikuid."

# Muutuja täishäälikute arvu salvestamiseks
vowl = 0

# Täishäälikud
vowls = "aeiouõäöü"

# Loome tsükli, mis käib läbi iga täht tekstis
for letter in text:
    # Kontrollime, kas täht on täishäälik
    if letter.lower() in vowls:
        vowl += 1

# Väljastame täishäälikute arvu
print("Täishäälikute arv tekstis:", vowl)
