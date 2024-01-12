from scraper import get_product_info
from data import export_product_info_to_csv


# Menu
print("Bienvenido/a al scraper de precios.")

choice = True
product_list = []

while(choice):
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

    # Get product's information from website
    product_info = get_product_info(product)

    # Check if the product has been previously consulted and is part of the list of products
    if product_info not in product_list:
        product_list.append(product_info)
        print("Informacion de producto obtenida correctamente.")
    else:
        print("Este producto fue consultado previamente.")

    print("")
    print("¿Te gustaría consultar otro producto?")
    answer = input("Sí (s)/No (n): ").lower()
    match answer:
        case "s":
            pass
        case "n":
            choice = False


print("Esta es la informacion obtenida del/los producto/s seleccionado/s: ")
print("")

for product in product_list:
    print(
        f'Nombre: {product["name"]}\nDescripcion: {product["description"]}\nPrecio: {product["price"]}\nCategoria: {product["category"]}\nImagen: {product["picture"]}\nEnlace: {product["url"]}'
    )
    print("")

print("")
print("¿Te gustaría exportar la informacion en un archivo CSV?")
answer_2 = input("Sí (s)/No (n): ").lower()

match answer_2:
    case "s":
        print("Exportando...")
        if export_product_info_to_csv(product_list):
            print("¡La información ha sido exportada correctamente!")
            print("¡Gracias por utilizar la aplicacion!")
        else:
            print("Ha ocurrido un problema. Por favor intentalo de nuevo.")
    case "n":
        print("¡Gracias por utilizar la aplicacion!")
    case _:
        print("Por favor, introduce una respuesta válida.")