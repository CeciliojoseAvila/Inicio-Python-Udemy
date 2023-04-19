class Restaurant:
    # constructor:
    def __init__(self, nombre, categoria, precio):
       self.nombre = nombre  # atributo
       self.categoria = categoria
       # default: public . PROTECTED(lleva raya al piso: _ ).rpivate(lleva doble guion bajo __ )
       self.__precio = precio

    def mostrar_informacion(self):
        print(
            f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}")

    # GETTER AND SETTER
    def get_precio(self):
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio

# clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)
hotel = Hotel("Hotel POO", "5 Estrellas", 500)
hotel.mostrar_informacion()