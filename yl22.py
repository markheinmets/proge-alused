# Kivi-paber-käärid mäng. 
# Arvuti mõtleb välja ühe variandi - kivi, paber või käärid.
# Arvuti küsib kasutaja valikut. Programm ütleb, kes võitis.
# Täienda programmi nii, et mängitakse seni, kuni kasutaja ei taha enam mängida.

import random

def winner(kasutaja, arvuti):
    if kasutaja == arvuti:
        return "Viik!"
    elif (kasutaja == "kivi" and arvuti == "käärid") or (kasutaja == "paber" and arvuti == "kivi") or (kasutaja == "käärid" and arvuti == "paber"):
        return "Kasutaja võidab!"
    else:
        return "Arvuti võidab!"

def kpk_game():
    valikud = ["kivi", "paber", "käärid"]

    while True:
        arvuti_valik = random.choice(valikud)
        kasutaja_valik = input("Vali kivi, paber või käärid (või sisesta 'exit', et lõpetada): ").lower()

        if kasutaja_valik == 'exit':
            print("Mäng lõpetatud.")
            break

        if kasutaja_valik not in valikud:
            print("Palun vali kivi, paber või käärid.")
            continue

        print(f"Arvuti valik: {arvuti_valik}")
        tulemus = winner(kasutaja_valik, arvuti_valik)
        print(tulemus)

if __name__ == "__main__":
    kpk_game()
