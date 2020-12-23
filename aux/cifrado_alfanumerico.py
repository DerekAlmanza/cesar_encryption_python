def cifrado_alfanumerico():
    desplazamiento = 3
    caracter_encripto = ""
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

            caracter_encripto = caracter_encripto + cifrado
        elif caracter.isupper():
            #Calcular índice del caracter en UNICODE
            caracter_indice = ord(caracter) - ord("A")

            #Saber cuánto se desplaza el índice del caracter
            desplazamient = (caracter_indice + desplazamiento) % 26

            #Convierte a nuevo caracter codificado
            nuevo_caracter = desplazamient + ord("A")
            cifrado = chr(nuevo_caracter)

            caracter_encripto = caracter_encripto + cifrado
        elif caracter.isdigit():
            #Calcular índice del caracter en UNICODE
            caracter_indice = (ord(caracter) + ord("Z")) - ord("A")

            #Saber cuánto se desplaza el índice del caracter
            desplazamient = (caracter_indice + desplazamiento) % 26

            #Convierte a nuevo caracter codificado
            nuevo_caracter = desplazamient + ord("A")
            cifrado = chr(nuevo_caracter)

            caracter_encripto = caracter_encripto + cifrado
        else:
            caracter_encripto += caracter

    print(caracter_encripto)

