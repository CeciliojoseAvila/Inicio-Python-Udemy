import os

CARPETA = 'contactos/'
EXTENSION = '.txt' # EXTENSION DE ARCHIVOS

#CONTACTOS:
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

# colocamos CARPETA donde hay 'contactos/'
def app():
    crear_directorio()

# Mostrar el menú de opciones
    mostrar_menu()

    # pregunatar al usuario
    pregunatar = True
    while pregunatar:
        opcion = input('seleccione del menú una opcion: \r\n')
        opcion = int(opcion)

    # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            pregunatar = False
        elif opcion == 2:
            editar_contacto()
            pregunatar = False
        elif opcion == 3:
            mostrar_contactos()
            pregunatar = False
        elif opcion == 4:
            buscar_contacto()
            pregunatar = False
        elif opcion == 5:
            eliminar_contacto()
            pregunatar = False
        else:
            print('Opcion no valida, intente de nuevo')


def eliminar_contacto():
        nombre = input('Escriba el contacto a Eliminar: \r\n')

        try:
            os.remove(CARPETA + nombre + EXTENSION)
            print('\r\n --> Contacto Eliminado Correctamente: \r\n')            
        except IOError:
            print('No existe ese contacto')

        # REINICIAR LA APP
        app()


def buscar_contacto():
    nombre = input('Escriba el contacto a buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
    except IOError:
        print('El archivo no existe')

    # REINICIAR LA APP
    app()

def mostrar_contactos():    
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open(CARPETA + archivo ) as contacto:
            for linea in contacto:
                # imprime los contenidos
                print(linea.rstrip())
                

def editar_contacto():
    print("Escribe el nombre del contacto a editar")
    nombre_anterior = input("Nombre del contacto a editar: \r\n")

    # VALIDAR SI ARCHIVO O USUARIO YA EXISTE, ANTES DE EDITARLO
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('Agrega el Nuevo Nombre: \r\n')
            telefono_contacto = input('Agrega el Nuevo Telefono: \r\n')
            categoria_contacto = input('Agrega la Nueva Categoria: \r\n')
            # INSTANCIAR
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            # ESCRIBIR EN EL ARCHIVO:
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

        # RENOMBRAR EL ARCHIVO
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
        # MOSTRAR MENSAJE DE EXITO
        print('\r\n Contacto Editado Correctamente \r\n')
    else:
        print('Ese contacto no existe')
    
    # REINICIAR LA APP
    app()

def agregar_contacto():
    print("Escribe los datos para agragar el nuevo contacto")
    nombre_contacto = input('Nombre del contacto: \r\n')

    # VALIDAR SI ARCHIVO O USUARIO YA EXISTE, ANTES DE CREARLO
    existe = existe_contacto(nombre_anterior)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            
            # RESTO DE LOS CAMPOS DE CONTACTO:
            telefono_contacto = input('Agrega el telefono: \r\n')
            categoria_contacto = input('Categoria Contacto: \r\n')

            #INSTANCIAR LA CLASE
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            # ESCRIBIR EN EL ARCHIVO:
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            # mostrar un mensaje de exito.
            print('\r\n Contacto creado Correctamente \r\n')
    else:
        print('Ese contacto ya existe -->')
    # REINICIAR LA APP
    app()

def mostrar_menu():
    print('Seleccione del menú lo que desea hacer: ')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        #crear la carpeta:
     os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()