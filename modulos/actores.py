import os
import funciones.corefile as cf

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

def gestor_actores():
    os.system('cls')
    id_p = (input('ingrese la id de la pelicula: '))
    nombre = input('ingrese el nombre de la pelicula: ')
    duracion = float(input('ingrese la duracion la pelicula: '))
    sipnosis = input('Ingrese la sipnosis de la pelicula: ')
    
    
    

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

def listar():
    if bd in bd['blockbuster']['actores']:
        print(bd['blockbuster']['actores'])
    