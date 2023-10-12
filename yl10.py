# yl10
# Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, 
# kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse,
# kui vanus on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, 
# kui vanus on 18, siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18,
# siis ütleb, et kasutaja võib autot juhtida. (sõne - string)


a = input("Mis on sinu nimi? ")
print("Tere,", a)
b = input("Kus sa elad? ")
D = ("Saaremaal")
if (b == D) :
    print("Väga äge!")
else:
    print("Alrighty")
c = int(input("Kui vana sa oled? "))
if (c <= 17) :
    print("Kahjuks oled sa liiga noor, et autot juhtida.")
elif (c == 18) :
    print("Palju õnne täisikka jõudmise puhul!")
else:
    print("Super, lubade olemas olemisel, võid juhtida autot!")