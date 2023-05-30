import json

# Nombre del archivo JSON para almacenar los favoritos
archivo_favoritos = "favoritos.json"

def cargar_favoritos():
    try:
        with open(archivo_favoritos, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_favoritos(favoritos):
    with open(archivo_favoritos, "w") as archivo:
        json.dump(favoritos, archivo)

def agregar_favorito():
    titulo = input("Ingrese el título: ")
    url = input("Ingrese la URL: ")
    comentario = input("Ingrese el comentario: ")

    favorito = {
        "titulo": titulo,
        "url": url,
        "comentario": comentario
    }

    favoritos = cargar_favoritos()
    favoritos.append(favorito)
    guardar_favoritos(favoritos)

    print("Favorito agregado con éxito.")

def eliminar_favorito():
    titulo = input("Ingrese el título del favorito a eliminar: ")

    favoritos = cargar_favoritos()
    favoritos = [favorito for favorito in favoritos if favorito["titulo"] != titulo]
    guardar_favoritos(favoritos)

    print("Favorito eliminado con éxito.")

def modificar_favorito():
    titulo = input("Ingrese el título del favorito a modificar: ")
    nuevo_titulo = input("Ingrese el nuevo título: ")
    nuevo_url = input("Ingrese el nuevo URL: ")
    nuevo_comentario = input("Ingrese el nuevo comentario: ")

    favoritos = cargar_favoritos()
    for favorito in favoritos:
        if favorito["titulo"] == titulo:
            favorito["titulo"] = nuevo_titulo
            favorito["url"] = nuevo_url
            favorito["comentario"] = nuevo_comentario
            break
    guardar_favoritos(favoritos)

    print("Favorito modificado con éxito.")

def ver_favoritos():
    favoritos = cargar_favoritos()

    if favoritos:
        print("Lista de Favoritos:")
        for favorito in favoritos:
            print("Título:", favorito["titulo"])
            print("URL:", favorito["url"])
            print("Comentario:", favorito["comentario"])
            print("---------------")
    else:
        print("No hay favoritos almacenados.")

def mostrar_menu():
    menu = """
    Menú:
    1. Agregar favorito
    2. Eliminar favorito
    3. Modificar favorito
    4. Ver la lista de favoritos
    5. Salir
    """

    print(menu)

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_favorito()
        elif opcion == "2":
            eliminar_favorito()
        elif opcion == "3":
            modificar_favorito()
        elif opcion == "4":
            ver_favoritos()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
