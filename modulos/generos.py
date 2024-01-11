import os
import funciones.corefile as cf

def crearGenero():
    genre = {
    'id' : '',
    'nombre_G': '',
    }
    id = input('ingrese la id de la pelicula: ')
    nombre_G = input('ingrese el genero de la pelicula: ')
    genre['id'] = id
    genre['nombre_G'] = nombre_G

    bd = {
        'blockbuster': {
            'peliculas':{
                'id_p': '',
                'nombre': '',
                'duracion': '',
                'sipnosis': '',
                'generos': {}
            },
            'actores':{
                'id_p': '',
                'nombre' : '',
                'rol':''
            },
            'formato':{
                'id_p': '',
                'nombre': '',
                'nroCopias': '',
                'valorPrestamo': ''
            }
        }
    }
    blockB = cf.check_file(bd)
    if blockB is not None and len(blockB)>0:
        if blockB == [{}]:
            for i, item in enumerate(blockB):
                blockB[i] = bd
                cf.save_file(blockB)
                os.system('pause')
                break
        else:
            blockB.append(bd)
            cf.save_file(blockB)
            os.system('pause')
    return blockB