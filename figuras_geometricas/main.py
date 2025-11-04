from core.models.rectangulo import Rectangulo

def main():
    rectangulo = Rectangulo(10, 10)
    print(f"Area {rectangulo.calcular_area()}")
    
if __name__=="__main__":
    main()