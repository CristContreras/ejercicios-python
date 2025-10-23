class Serie:
    def __init__(self, titulo, productor, anio):
        self.__titulo = titulo
        self.__anio=anio
    
    @property
    def titulo(self):
        return self.__titulo
    
    def __str__(self):
        return f"Titulo {self.__titulo} - Año {self.__anio}"

