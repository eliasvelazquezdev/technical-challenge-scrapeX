# Technical challenge (ScrapeX) - Webscraping with Python

App that scraps products information from a given supermarket website and then, if user decides to, export this information to a csv file.

## Tools

 - Selenium 4
 - XPath
 - Python's built-in CSV module

## Installation

1) Install virtualenv globally using pip
   ```
   python -m pip install virtualenv
   ```
   
2) Create a virtual environment with virtualenv
   ```
   python virtualenv env_name
   ```
   
3) Activate the virtual environment
   ```
   // For Linux
   source env_name/bin/activate

   // For Windows
   .\env_name\Scripts\activate
   ```

4) Install the dependencies
   ```
   pip install -r requirements.txt
   ```

## How to use it
When you run the main.py file, a menu whill show up on the console greeting you with a welcome message.

You'll have to choose which product (out of 3) you'd like to get information from by typing the corresponding number.

You can gather information from 1 to 3 products in the same session. The app will add every consulted product into a product list.

If you attempt to retrieve information from the same product twice in the same session, the app will notify you. This prevents duplicates in the product list, and therefore, in the CSV file if you decide to export the information.

After obtaining the necessary information, you can choose to export it into a CSV file named "products.csv".

## Documentation

### Approach
**Why Selenium?**<br>
Selenium has a lot of features that I've found interesting when tackling this challenge, like the waiting times that allows certain HTML to be fully loaded,  and simulation of user's actions like clicks, or drag and drop, among other things.

Another great reason is that Selenium allows you to locate and select elements in a website using multiple methods. One of those methods is XPath.

<br>

**Why XPath?**<br>
I've found XPath to be a precise and versatile tool for data extraction. Dynamic websites (like the one stores and supermarkets have) are higly nested webpages and tend to change its structure frequently. XPath allows you to traverse these kind of websites by selecting nodes and attributes, like CSS classes or IDs. 

For instance, during the development of this solution, an HTML element (span) containing the product's price changed its CSS class because the product was on discount. Thanks to XPath node selection, I didn't have to change the way I was accesing the element because I targeted the element with the "contains" function, that checks if a given sub-string is contained inside a CSS class name. 

### Functions

**get_product_info(product: str) -> str**<br>
This function (that lives in the "scraper" script) takes a string with a product name (like the one you choose from the main menu) and types it into a search bar on a supermarket website (Coto Digital).

Using Selenium's built-in Xpath method, it will try to find the search bar and then all the HTML elements containing product's information.

After gathering the neccesary information (name, description, price, category, picture, url), it will return a dictionary containing these values.

Note that this function has some waiting times using Selenium's *WebDriverWait* class and Python's built-in *time* module to allow HTML to be properly loaded and visible, avoiding errors when trying to locate such elements.

<br>

**export_product_info_to_csv(product_list: list) -> bool**<br>
Function inside the "data" script that takes a list as an argument and then iterates over it and saves the content into a csv file.

The list must contain dictionaries as items so the *DictWriter* class can write rows into the CSV file. Otherwise it will raise an exception.

The function also checks if the csv file exists. If it does, it will append new information without duplicating the headers (column names). If the file doesn't exist, it will write the headers and product's information.

Returns *True* if the export process was successful.
