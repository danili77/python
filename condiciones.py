a = 35
b = 33

if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")

if a > b: print("a es mayor que b")   # en una sola linea


a = 2
b = 330
print("A") if a > b else print("B")


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


a = 200
b = 33
c = 500
if a > b and c > a: # ambas condiciones
  print("Both conditions are True")

# if anidado
 x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a = 33
b = 200

if b > a:
  pass     # para evitar errores
