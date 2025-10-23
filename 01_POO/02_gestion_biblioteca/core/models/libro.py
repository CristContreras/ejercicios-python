class Libro:
    def __init__(self, titulo: str, autor: str, isbn: int):
        self.__titulo: str=titulo
        self.__autor:str=autor
        self.__isbn:int=isbn
        self.__disponible:bool=True
        self.__dias_prestamo=0
    
    def prestar_libro(self):
        self.__disponible=False
        #registrar fecha
    
    def devolver_libro(self):
        