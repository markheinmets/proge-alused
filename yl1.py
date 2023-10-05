#yl1
#Kirjuta programm, mis teisendab kasutaja poolt kroonides sisestatud summa eurodesse ja väljastab ümardatud tulemuse. (round)

eek = input("Sisesta kroonid: ")
eur = eek = float(eek) / 15.6466
print(round(eur, 2))