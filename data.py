import csv

# Function to execute when this script is run instead of imported
def main_greeting():
    return "Executing script"


def export_product_info_to_csv(product_info: dict):
    """
    Takes a dictionary with product information as an argument and saves values into a CSV file
    """
    try:
        with open('productos.csv', 'w') as csvfile:
            fieldnames = ["Producto", "Descripcion", "Precio", "Categoria", "Imagen", "Enlace"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Write header (first row)
            writer.writeheader()
            writer.writerow({
                "Producto" : product_info["name"],
                "Descripcion" : product_info["description"],
                "Precio" : product_info["price"],
                "Categoria" : product_info["category"],
                "Imagen" : product_info["picture"],
                "Enlace" : product_info["url"]
            })
            return True
    except Exception as e:
        print("Error!", e)



if __name__ == "__main__":
    main_greeting()

