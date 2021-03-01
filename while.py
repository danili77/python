i = 1

while i < 6:
    print(i)
    i= i+1


while i < 6:
    print(i)
    if i == 3:
        break  # detener el ciclo
    i = i + 1



i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)


i = 1
while i < 6:
    print(i)
    i = i + 1
else:
    print("i no es menos de 6")    
