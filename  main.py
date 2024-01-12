from scraper import get_product_info
from data import export_product_info_to_csv


# Menu
print("Welcome to the product scraper!")

choice = True
product_list = []

while(choice):
    print("These are the available products:")
    print("")
    print("1. Gaseosa Coca Cola 2.5lt")
    print("2. Gaseosa Coca Cola 2.25lt")
    print("3. Gaseosa Coca Cola Sabor Original 500ml")

    print("")
    option = input("Choose which product you'd like to get information from by typing the corresponding number.")

    print("Retrieving information...")
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
        print("Product information retrieved correctly.")
    else:
        print("This product was already consulted!")

    print("")
    print("Would you like to choose another product?")
    answer = input("Yes (y)/No (n): ").lower()
    match answer:
        case "y":
            pass
        case "n":
            choice = False


print("This is the information about the selected product/s: ")
print("")

for product in product_list:
    print(
        f'Nombre: {product["name"]}\nDescripcion: {product["description"]}\nPrecio: {product["price"]}\nCategoria: {product["category"]}\nImagen: {product["picture"]}\nEnlace: {product["url"]}'
    )
    print("")

print("")
print("Would you like to export the information into a csv file?")
answer_2 = input("Yes (y)/No (n): ").lower()

match answer_2:
    case "y":
        print("Exporting...")
        if export_product_info_to_csv(product_list):
            print("Information exported successfully!")
            print("Thank you for using the app!")
        else:
            print("A problem has occurred! Please try again.")
    case "n":
        print("Thank you for using the app!")
    case _:
        print("Please introduce a valid answer. Aborting...")