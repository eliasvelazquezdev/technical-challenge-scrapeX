import csv
import os

# Function to execute when this script is run instead of imported
def main_greeting():
    return "Executing script"


def export_product_info_to_csv(product_list: list) -> bool:
    """
    Takes a list with dictionaries containing product information as an argument and saves values into a CSV file
    Returns true is the csv export is successful
    """

    filename = 'productos.csv'
    file_exists = os.path.isfile(filename)

    try:
        with open(filename, 'a+') as csvfile:
            fieldnames = ["Producto", "Descripcion", "Precio", "Categoria", "Imagen", "Enlace"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists: 
                # Write header (first row)
                writer.writeheader()
                
            for product_info in product_list:
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

