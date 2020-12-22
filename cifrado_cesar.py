def cifrado_mayus():
    desplazamiento = 3
    encryption = ""
    texto = input("Ingrese cadena de texto a cifrar: ")
    for caracter in texto:
        if caracter.isupper():
            #Calcular índice del caracter en UNICODE
            caracter_indice = ord(caracter) - ord("A")

            #Saber cuánto se desplaza el índice del caracter
            desplazamient = (caracter_indice + desplazamiento) % 26

            #Convierte a nuevo caracter codificado
            nuevo_caracter = desplazamient + ord("A")
            cifrado = chr(nuevo_caracter)

            encryption = encryption + cifrado
        else:
            encryption += caracter


def cifrado_minus():
    desplazamiento = 3
    encryption = ""
    texto = input("Ingrese cadena de texto a cifrar: ")
    for caracter in texto:
        if caracter.islower():
            #Calcular índice del caracter en UNICODE
            caracter_indice = ord(caracter) - ord("a")

            #Saber cuánto se desplaza el índice del caracter
            desplazamient = (caracter_indice + desplazamiento) % 26

            #Convierte a nuevo caracter codificado
            nuevo_caracter = desplazamient + ord("a")
            cifrado = chr(nuevo_caracter)

            encryption = encryption + cifrado
        else:
            encryption += caracter
    
    print(encryption)


if __name__ == "__main__":
    cifrado_mayus()