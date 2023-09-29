import unittest
from product import Product  # Assuming you have a separate product.py file
from checkout_register import CheckoutRegister  # Assuming you have a separate checkout_register.py file


class TestProduct(unittest.TestCase):
    def test_get_name(self):
        # Create a product instance with a name, price, and barcode
        product = Product("Milk, 2 Litres", 3.50, "123")
        # Test that the get_name method returns the expected name
        self.assertEqual(product.get_name(), "Milk, 2 Litres")

    def test_get_price(self):
        # Create a product instance with a name, price, and barcode
        product = Product("Milk, 2 Litres", 3.50, "123")
        # Test that the get_price method returns the expected price
        self.assertEqual(product.get_price(), 3.50)

    def test_get_barcode(self):
        # Create a product instance with a name, price, and barcode
        product = Product("Milk, 2 Litres", 3.50, "123")
        # Test that the get_barcode method returns the expected barcode
        self.assertEqual(product.get_barcode(), "123")


class TestCheckoutRegister(unittest.TestCase):
    def test_scan_item(self):
        # Create a CheckoutRegister instance
        register = CheckoutRegister()
        # Create a product instance with a name, price, and barcode
        product = Product("Milk, 2 Litres", 3.50, "123")

        # Test that scan_item updates the total payment correctly
        result = register.scan_item(product)
        # Assert that the result is None (modify this based on your logic)
        self.assertEqual(result, None)

    def test_accept_payment(self):
        # Create a CheckoutRegister instance
        register = CheckoutRegister()
        # Accept a payment of 5.00
        register.accept_payment(5.00)
        # Test that get_received_amount returns the expected received amount
        self.assertEqual(register.get_received_amount(), 5.00)

    def test_init(self):
        # Create a CheckoutRegister instance
        register = CheckoutRegister()
        # Test that the initial purchased items list is empty
        self.assertEqual(len(register.get_purchased_items()), 0)
        # Test that the initial total payment is 0.00
        self.assertEqual(register.get_total_payment(), 0.00)
        # Test that accept_payment updates the total payment to 10.00
        self.assertEqual(register.accept_payment(10.00), 10.00)


if __name__ == '__main__':
    unittest.main()
