x = 7

y = 2

z = 3

# Operadores aritmeticos

print(x + y) # suma

print(x - y)# resta

print(x * y) # multiplicación

print(x / y) # division

print(x % y) # modulo

print(x ** y) # exponenciación o elevacion

print(x // y) # division de piso --> redondea el resultado al numero entero mas cercano

# Operadores de Asignación

#print(x = 5)


x = x + 3  # igual que x += 3

print(x)

x = x - 3 # igual que x -= 3

print(x)

x = x * 3 #igual que x *= 3

print(x)

x = x / 3 # igual que x /= 3

print(x)


x = x % 3 # igual que x %= 3

print(x)

x = x // 3 # igual que x //= 3

print(x)

x = x ** 3 #igual que x **= 3

print(x)

#x = x & 3 # igual que x &= 3

print(x)

#x = x | 3 # igual que x |= 3

print(x)

z = z ^ 3

print(z)

z = z >> 3 # igual que x >>= 3

print(z)

z = z << 3  # igual que x <<= 3

print(z)

# Operadores de comparación

print(x == y)  #igual

print(x != y) # no igual o distinto

print(x > y) # mayor que

print(x < y) # menor que

print(x >= y) # mayor o igual que

print(x <= y) # menor o igual que

# Operadores booleanos

print(x < 5 and x < 10) # devuelve true si ambas partes son true

print(x < 5 or x < 4) # devuelve true si ua parte es true

print(not(x < 5 and x < 10)) #devuelve false si el resultado es true

# Operadores de identidad--> para comparar objetos

print(x is y) #devuelve true si ambas variables son el mismo objeto

print(x is not y) # devuelve true si ambas variables no son el mismo objeto


# Operadores de membresia o pertenencia --> para probar si se presenta una secuencia en un objeto
a = "banana"

b = ["manzana", "banana"]

print(a in b)

print(a not in  b)

 # Operadores bit a bit --> se usan para comparar numeros binarios(101)

 # & and --> Establece cada bit en 1 si ambos bits son 1.
 # | or --> Establece cada bit en 1 si uno de los dos bits es 1
 # ^ xor --> Establece cada bit en 1  si solo uno de los dos bits es 1
 # ~ not --> invierte todos los bits
 # << Desplazamiento a la izquierda de llenado cero --> Desplácese hacia la izquierda presionando ceros desde la derecha y deje que los bits de la izquierda se caigan
 # >> cambio a la derecha --> Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
