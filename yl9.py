# yl9
# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks,
# võrdhaarseteks ja võrdkülgseteks. Kirjutada programm,
# mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi.
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida.
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

a = input("üks külg: ")
b = input("teine külg: ")
c = input("kolmas külg: ")
if (float(a) == float(b) == float(c)) :
    print("võrdkülgne kolmnurk")
elif float(a) == float(b) != float(c) or float(a) == float(c) != float(b) or float(b) == float(c) != float(a) :
    print("võrdhaarne kolmnurk")
elif float(a) + float(b) == float(c) or float (a) + float(c) == float(b) or float(b) + float(c) == float(a) :
    print("kolmnurka ei eksisteeri")
else:
    print("erikülgne kolmnurk")