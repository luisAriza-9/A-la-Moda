import os
import funciones.corefile as cf
cf.RUTA = 'data/blockbuster.json'
pelicula = {
}
def gestor_actores():
    id_p = (input('ingrese la id de la pelicula: '))
    nombre = input('ingrese el nombre de la pelicula: ')
    duracion = float(input('ingrese la duracion la pelicula: '))
    sipnosis = input('Ingrese la sipnosis de la pelicula: ')
    genre = {
        'id' : id,
        'nombre_G': nombre_G,
    }
    id = int(input('ingrese la id de la pelicula: '))
    nombre_G = input('ingrese el genero de la pelicula: ')
    genre['id'] = id
    genre['nombre_G'] = nombre_G


    bd = {
        'blockbuster': {
            'peliculas':{
                'id_p': id_p,
                'nombre': nombre,
                'duracion': duracion,
                'sipnosis': sipnosis,
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
    return pelicula

def search():
    data = cf.open_file()
    id = input('ingrse')