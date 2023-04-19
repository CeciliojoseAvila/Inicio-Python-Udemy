class Restaurant:
    # constructor:
    def __init__(self, nombre, categoria, precio):
       self.nombre = nombre  # atributo
       self.categoria = categoria
       # default: public . PROTECTED(lleva raya al piso: _ ).rpivate(lleva doble guion bajo __ )
       self.precio = precio

    def mostrar_informacion(self):
        print(
            f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}")

    # GETTER AND SETTER
    def get_precio(self):
        print(self.precio)

    def set_precio(self, precio):
        self.precio = precio

# clase hijo de Restaurant

class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca

# Reescribir un metodo, debe llamarse igual
    def mostrar_informacion(self):
        print(
            f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio},Alberca: {self.alberca}")

#AGREGAR METODO QUE SOLO EXISTA EN HOTEL
    def get_alberca(self):
        return self.alberca
        
hotel = Hotel("Hotel POO", "5 Estrellas", 500, "SI")
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)
