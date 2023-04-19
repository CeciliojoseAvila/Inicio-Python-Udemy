def app():
    # crear el archivo
    archivo = open('archivo.txt', 'w') # w es de escritura, si no existe lo creara
    for i in range(0, 21):
        archivo.write('Esta es la linea ' +str(i) + "\r\n")
    # es necesario cerrar los archivos, sino python los dejará abiertos
    archivo.close()

app()