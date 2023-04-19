class Restaurant:
    #constructor:
    def __init__(self, nombre, categoria, precio):
       self.nombre = nombre  # atributo
       self.categoria = categoria
       self.precio = precio

    def mostrar_informacion(self):
        print(
            f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}")

# instanciar la clase
restaurant = Restaurant("Pizzeria Colombia", "la mejor comida", 18500)
restaurant.mostrar_informacion()

restaurant2 = Restaurant("Hamburguesas python", "comida casual", 15000)
restaurant2.mostrar_informacion()
