# Menu

print("Bienvenido/a al scraper de precios.")
print("Estos son los productos disponibles:")
print("")
print("1. Gaseosa Coca Cola 2.5lt")
print("2. Gaseosa Coca Cola 2.25lt")
print("3. Gaseosa Coca Cola Sabor Original 500ml")

print("")
option = input("Selecciona el producto del cual te gustaría recibir información: ")
product = None

match option:
    case "1":
        product = "Gaseosa Coca Cola 2.5 L"
    case "2":
        product = "Gaseosa Coca Cola 2.25 L"
    case "3":
        product = "Gaseosa Coca Cola Sabor Original 500 Ml"