playlist = {}
playlist['canciones']= []

def app():       
    agregar_playlist = True    
    while agregar_playlist:
        nombre_playlist = input('¿Cómo deseas nombrar la playlist?\r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False              
            print(playlist)

            #AGREGAR NUEVAS CANCIONES
        agregar_canciones()
def agregar_canciones():
        agregar_cancion = True
        while agregar_cancion:
            nomabre_playlist = playlist['nombre']
            pregunta = f'Agrega canciones a {nomabre_playlist}\r\n'
            pregunta += 'Escribe "x" para dejar de agregar canciones:\r\n'

            cancion = input(pregunta)
            
        if cancion == 'x':
            print("cerrar")            
        else:
            playlist['canciones'].append(cancion)       
                 
app()
