import funciones.corefile as cf
import modulos.peliculas as p
import os

opciones = ['Administrador de generos','Administrador de actores','Adminstrador de formatos','Gestor de informes','Gestor de peliculas','Salir']
opGeneros = ['crear genero','Listar generos','Menu principal']
opActores = ['crear actor','Listar actores','Menu principal']
opFormatos = ['crear Formatos','Listar Formatos','Menu principal']
opPeliculas = ['Agregar pelicula','Editar pelicula','Eliminar pelicula','Eliminar Actor','Buscar pelicula','Listar todas las peliculas','Menu principal']
opInformes = []



def menu_principal():
    p.cf.check_file(p.pelicula)
    os.system('cls')
    header = """
    ******************************************
    * SITEMA GESTOR DE PELICULAS BLOCKBUSTER *
    ******************************************
    """
    print(header)
    for i,item in enumerate(opciones):
            print(f'{(i + 1)} - {item}')

def menu_gestosPeliculas():
    isActiveP = True
    tittle = """
    ***********************
    * GESTOR DE PELICULAS *
    ***********************
    """
    while (isActiveP):
        os.system('cls')
        print(tittle)
        for i, item in enumerate(opPeliculas):
             print(f'{( i + 1)} - {item}')
        try:
             op = int(input(':)'))
        except ValueError:
             print('Error en el dato ingresado')
        else:
            if(op == 1):
                pass
            elif(op == 2):
                pass
            elif(op == 3):
                pass
            elif(op == 5):
                pass
            elif(op == 6):
                pass
            elif(op == 7):
                isActiveP = False

