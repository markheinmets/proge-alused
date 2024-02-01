# Kaardimäng Blackjack

# https://et.wikipedia.org/wiki/Blackjack


import random

def uued_kaardid():
    mastid = ['Ärtu', 'Ruutu', 'Risti', 'Poti']
    nimed = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Poiss', 'Emand', 'Kuningas', 'Äss']
    kaardid = [{'Nimetus': nimi, 'Mast': mast} for mast in mastid for nimi in nimed]
    random.shuffle(kaardid)
    return kaardid

def punktid_käes(kaardid):
    punktid = 0
    aces = 0

    for kaart in kaardid:
        punktid += min(10, nimetus_punktideks(kaart['Nimetus']))

        if kaart['Nimetus'] == 'Äss':
            aces += 1

    while aces > 0 and punktid + 10 <= 21:
        punktid += 10
        aces -= 1

    return punktid

def nimetus_punktideks(nimetus):
    if nimetus in ['Poiss', 'Emand', 'Kuningas']:
        return 10
    elif nimetus == 'Äss':
        return 11
    else:
        return int(nimetus)

def blackjack_mang():
    kaardipakk = uued_kaardid()
    mängija_kaardid = [kaardipakk.pop(), kaardipakk.pop()]
    diileri_kaardid = [kaardipakk.pop(), kaardipakk.pop()]

    while True:
        print(f'Mängija kaardid: {mängija_kaardid}, Punktid: {punktid_käes(mängija_kaardid)}')
        print(f'Diileri esimene kaart: {diileri_kaardid[0]}')

        if punktid_käes(mängija_kaardid) == 21:
            print('Blackjack! Mängija võidab!')
            break

        valik = input("Kas soovid võtta kaardi (vajuta 'k') või seista (vajuta 's'): ").lower()

        if valik == 'k':
            mängija_kaardid.append(kaardipakk.pop())

            if punktid_käes(mängija_kaardid) > 21:
                print('Üle 21 punkti! Mängija kaotas.')
                break
        elif valik == 's':
            while punktid_käes(diileri_kaardid) < 17:
                diileri_kaardid.append(kaardipakk.pop())

            print(f'Diileri kaardid: {diileri_kaardid}, Punktid: {punktid_käes(diileri_kaardid)}')

            if punktid_käes(diileri_kaardid) > 21:
                print('Diiler üle 21 punkti! Mängija võidab!')
            elif punktid_käes(mängija_kaardid) > punktid_käes(diileri_kaardid):
                print('Mängija võidab!')
            elif punktid_käes(mängija_kaardid) < punktid_käes(diileri_kaardid):
                print('Diiler võidab!')
            else:
                print('Viik!')

            break
        else:
            print('Palun sisesta kehtiv valik (k või s).')

if __name__ == "__main__":
    blackjack_mang()
