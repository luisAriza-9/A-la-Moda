import os
import iu.menu as mn
import modulos.peliculas as b

while True:
    os.system('cls')
    menu = mn.menu_principal() 
    try:
        op = int(input(':)'))
    except ValueError:
        print('Error en el dato ingresado')
    else:
        if(op == 1):
            pass
        elif(op == 2):
            b.gestor_actores()
        elif(op == 3):
            pass
        elif(op == 4):
            pass
        elif(op == 5):
            pass
        elif(op == 6):
            print('Adios, gracias por visitarnos!!')
            input('Presione any key....')
            break