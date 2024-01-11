import os
import funciones.corefile as cf
cf.RUTA = 'data/blockbuster.json'
pelicula = {
}
def add_movie():
    id_p = input('ingrese la id de la pelicula: ')
    nombre = input('ingrese el nombre de la pelicula: ')
    duracion = input('ingrese la duracion la pelicula: ')
    sipnosis = input('Ingrese la sipnosis de la pelicula: ')
    

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
    campus = cf.check_file(bd)
    if campus is not None and len(campus)>0:
        if campus == [{}]:
            for i, camper in enumerate(campus):
                campus[i] = bd
                cf.save_file(campus)
                os.system('pause')
                break
        else:
            campus.append(bd)
            cf.save_file(campus)
            os.system('pause')
    return bd

def search():
    data = cf.open_file()
    id = input('ingrse')