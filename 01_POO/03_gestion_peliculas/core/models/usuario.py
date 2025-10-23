from .serie import Serie

class Usuario:
    def __init__(self, nombre, id):
        self.__nombre=nombre
        self.__id=id
        self.__series_vistas: list[Serie]=[]    

    def ver_serie(self, serie:Serie):
        if not any(serie_h.titulo == serie.titulo for serie_h in self.__series_vistas):
            self.__series_vistas.append(serie)

    
    @property
    def series_vistas(self):
        return self.__series_vistas