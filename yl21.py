# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani.
# Lase kasutajal pakkuda, mis arvu arvuti välja mõtles.
# Vale pakkumise korral annab arvuti vihje,
# kas pakkumine on õigest arvust suurem või väiksem.
# Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)

import random

# Arvuti mõtleb välja juhusliku arvu vahemikus 0 kuni 100
random_number = random.randint(0, 101)

# Alguses pole kasutaja veel õiget arvu ära arvanud
user_guess = None

# Mäng käib seni, kuni kasutaja ei arva õiget arvu ära
while user_guess != random_number:
    # Küsime kasutajalt pakkumist
    user_guess = int(input("Paku arv 0 kuni 100: "))

    # Kontrollime kasutaja pakkumist ja anna vastav vihje
    if user_guess < random_number:
        print("Arv on suurem, proovi uuesti.")
    elif user_guess > random_number:
        print("Arv on väiksem, proovi uuesti.")
    else:
        print(f"Õige! Arvuti mõtles arvu {random_number}.")
