# Define the Product class to represent a product in the store.
class Product:
    # The constructor (init method) initializes the product with a name, price, and barcode.
    def __init__(self, name, price, barcode):
        self.__name = name  # Product name
        self.__price = price  # Product price
        self.__barcode = barcode  # Product barcode

    # Getter method to get the product's name.
    def get_name(self):
        return self.__name

    # Getter method to get the product's price.
    def get_price(self):
        return self.__price

    # Getter method to get the product's barcode.
    def get_barcode(self):
        return self.__barcode

    # String representation of the Product object
    def __str__(self):
        return f"Barcode: {self.__barcode}\nProduct Name: {self.__name}\nPrice: ${self.__price:.2f}"
