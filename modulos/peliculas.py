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
            for i in enumerate(campus):
                campus[i] = bd
                cf.save_file(campus)
                os.system('pause')
                break
        else:
            campus.append(bd)
            cf.save_file(campus)
            os.system('pause')
    return pelicula

def search():
    data = cf.open_file()
    id = input('ingrese la pelicula a buscar: ')
    if pelicula.get('id') == id:
        print(pelicula['blockbuster']['peliculas'])
    else:
        print('No se encontro ese id')

def delete():
    data = cf.open_file()
    id = input('ingrese la pelicula a eliminar: ')
    for i,c in enumerate(data):
        if pelicula.get('id') == id:
            index_to_remove = i
            cf.eliminar(data,index_to_remove = index_to_remove)
            cf.save_file(data)


    
