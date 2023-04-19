class Restaurant:
    # constructor:
    def __init__(self, nombre, categoria, precio):
       self.nombre = nombre  # atributo
       self.categoria = categoria
       self.__precio = precio  # default: public . PROTECTED(lleva raya al piso: _ ).rpivate(lleva doble guion bajo __ )

    def mostrar_informacion(self):
        print(
            f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}")

    #GETTER AND SETTER
    def get_precio(self):
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio
        
# instanciar la clase
restaurant = Restaurant("Pizzeria Colombia", "la mejor comida", 18500)
# print(restaurant.__precio) comento para poder acceder a los private
#restaurant.__precio = 20000
restaurant.mostrar_informacion()
restaurant.set_precio(20000)
restaurant.get_precio()

restaurant2 = Restaurant("Hamburguesas python", "comida casual", 15000)
#print(restaurant.__precio) comento para poder acceder a los private
#restaurant2.__precio = 18000
restaurant2.mostrar_informacion()
restaurant2.set_precio(22000)
restaurant2.get_precio()
