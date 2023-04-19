class Restaurant:
    def agregar_restaurant(self, nombre):
        self.nombre = nombre #atributo
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        
# instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurant("Pizzeria Colombia")
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant("Hamburguesas python")
restaurant2.mostrar_informacion()
