cantidad = 3

numeroArticulo = 567

precio = 49.95

#miPedido = "quiero {} piezas del articulo {} con {} euros."
miPedido = "quiero {2} piezas del articulo {0} con {1} euros." # Utilizando los indices de las variables.
print(miPedido.format(cantidad,numeroArticulo,precio))
