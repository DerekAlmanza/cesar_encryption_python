import cifrado_alfabeto as cesar_abc
import cifrado_alfanumerico as cesar_123
import os

def menu_interfaz():

    os.system('clear')
    print ("""Programa diseñado para efectuar el cifrado Cesar de un texto.
                Selecciona una opción:\n""")
    print ("\t1 - Cifrar caracteres puramente mayúsculas.")
    print ("\t2 - Cifrar caracteres puramente minúsculas.")
    print ("\t3 - Cifrar caracteres ya sean mayúsculas o minúsculas.")
    print ("\t4 - Cifrar caracteres alfanuméricos.")
    print ("\t5 - Salir \n")

def quiere_repetir():
    print('\n ¿Desea realizar otra encriptación?')
    opcion = input('Teclee y/n para realizar otra encriptación o no: ')
    if opcion == "y":
        menu()
    elif opcion == "n":
        pass
    else:
        pass


def menu():
    while True:
        menu_interfaz()
        opcion = input("Inserte opcion: ")
        print('')
        if opcion == "1":
            cesar_abc.cifrado_mayus()
            quiere_repetir()
            break
        elif opcion == "2":
            cesar_abc.cifrado_minus()
            quiere_repetir()
            break
        elif opcion == "3":
            cesar_abc.cifrado_mayus_minus()
            quiere_repetir()
            break
        elif opcion == "4":
            cesar_123.cifrado_alfanumerico()
            quiere_repetir()
            break
        elif opcion == "5":
            break
        else:
            print("No has pulsado una opción valida.")

menu()