from scraper import get_product_info
from data import export_product_info_to_csv
import time

# Menu
print("Bienvenido/a al scraper de precios.")
print("Estos son los productos disponibles:")
print("")
print("1. Gaseosa Coca Cola 2.5lt")
print("2. Gaseosa Coca Cola 2.25lt")
print("3. Gaseosa Coca Cola Sabor Original 500ml")

print("")
option = input("Selecciona el producto del cual te gustaría recibir información. Introduce el numero correspondiente: ")

print("Consiguiendo información...")
product = None

match option:
    case "1":
        product = "Gaseosa Coca Cola 2.5 L"
    case "2":
        product = "Gaseosa Coca Cola 2.25 L"
    case "3":
        product = "Gaseosa Coca Cola Sabor Original 500 Ml"


product_info = get_product_info(product)

print("Esta es la informacion obtenida del producto seleccionado: ")
print("")
print(
    f'Nombre: {product_info["name"]}\nDescripcion: {product_info["description"]}\nPrecio: {product_info["price"]}\nCategoria: {product_info["category"]}\nImagen: {product_info["picture"]}\nEnlace: {product_info["url"]}'
)

print("")
print("¿Te gustaría exportar la informacion en un archivo CSV?")
answer = input("Sí (s)/No (n): ").lower()

match answer:
    case "s":
        print("Exportando...")
        if export_product_info_to_csv(product_info):
            print("¡La información ha sido exportada correctamente!")
        else:
            print("Ha ocurrido un problema. Por favor intentalo de nuevo.")
    case "n":
        print("¡Gracias por utilizar la aplicacion!")
    case _:
        print("Por favor, introduce una respuesta válida.")