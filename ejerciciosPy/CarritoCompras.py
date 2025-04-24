producto = input("Ingresa el nombre del producto: ")
cantidad = int(input("Cantidad: "))
carrito = {}

carrito[producto] = cantidad
if cantidad > 5:
    print(f"Venta al por mayor")
print(f"Carrito: {carrito}")
