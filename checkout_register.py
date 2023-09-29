from typing import List
from product import Product
from datetime import datetime

class CheckoutRegister:
    def __init__(self):
        self.__total_payment = 0.0
        self.__received_amount = 0.0
        self.__purchased_items = []
        self.__product_list = []

    def load_products(self, filename: str):
        self.__product_list.clear()
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if len(parts) == 2:
                    name = parts[0]
                    price = float(parts[1].replace('$', ''))
                    barcode = name[:3].upper()
                    self.__product_list.append(Product(name, price, barcode))

    def get_product(self, barcode: str) -> Product:
        for product in self.__product_list:
            if product.get_barcode() == barcode:
                return product
        return None

    def get_total_payment(self) -> float:
        return self.__total_payment

    def get_received_amount(self) -> float:
        return self.__received_amount

    def accept_payment(self, some_amount: float) -> float:
        self.__received_amount += some_amount
        return self.__received_amount

    def scan_item(self, some_product: Product):
        self.__total_payment += some_product.get_price()
        self.__purchased_items.append(some_product)

    def print_receipt(self):
        print("----- Final Receipt -----")
        for item in self.__purchased_items:
            print(f"{item.get_name()}\n$ {item.get_price():.2f}")
        print(f"Total amount due: $ {self.__total_payment:.2f}")
        print(f"Amount received: $ {self.__received_amount:.2f}")
        print(f"Balance given: $ {self.__received_amount - self.__total_payment:.2f}")

    def save_transaction(self, current_date: str, filename: str):
        with open(filename, "a") as file:
            for item in self.__purchased_items:
                file.write(f"{current_date}, {item.get_barcode()}, {item.get_price():.2f}\n")

    def get_purchased_items(self) -> List[Product]:
        return self.__purchased_items
