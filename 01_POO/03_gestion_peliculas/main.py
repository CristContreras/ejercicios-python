from core.models.serie import Serie
from core.models.usuario import Usuario

def main():
  una_serie = Serie("The office", "HBO", 1995)
  un_usuario=Usuario("Cris",1)


  un_usuario.ver_serie(una_serie)
  print("Viendo serie")
  print("Lista de series vistas")
  for serie in un_usuario.series_vistas:
     print(serie)


if __name__ == "__main__":
    main()

