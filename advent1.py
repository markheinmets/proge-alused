
f = open("input.txt")

in_str = f.read()

position = 0
floor = 0

for c in in_str :
    if c == "(" :
        position += 1
    else : 
        position -= 1


print(position)