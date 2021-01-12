import cifrado_alfanumerico as cesar_123

def cifrado_archivo(archivo_input,archivo_output):

    with open(archivo_input, "r") as archivo_entrada:
        with open(archivo_output, "w") as archivo_salida:
            for linea in archivo_entrada:
                linea_cifrada = cesar_123.cifrado_alfanumerico(linea)
                archivo_salida.write(linea_cifrada)
                

    print('El archivo {} ha sido cifrado y se ha escrito su cifrado en {}'.format(archivo_input,archivo_output))

print('''Este programa es un prototipo. Por el momento solo cifra archivos que 
    estén a la altura del archivo Main, por lo que recuerda comenzar el nombre
    de tu archivo con ./filename \n''')

archivo_input = input('Ingrese el nombre de archivo a cifrar: ')
archivo_output = input('Ingrese como quiere que se llame el archivo cifrado: ')

cifrado_archivo(archivo_input,archivo_output)



