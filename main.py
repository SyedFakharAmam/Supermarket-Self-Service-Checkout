from product import Product
from checkout_register import CheckoutRegister
from datetime import datetime
import sys

def main():
    product_list = []

    # Load product data from products.txt
    with open("products.txt", "rt") as file:
        for line in file:
            parts = line.strip().split(" - ")
            if len(parts) == 2:
                name = parts[0]
                price = float(parts[1].replace("$", ""))
                # Assuming the barcode is the first 3 characters of the name
                barcode = name[:3].upper()
                product_list.append(Product(name, price, barcode))

    while True:
        print("--- Welcome to the Grocery Store ---")
        checkout = CheckoutRegister()
        continue_shopper = 'y'

        while continue_shopper.lower() == 'y':
            while True:
                try:
                    barcode = input("Please enter the barcode (or 'end' to finish shopping): ")
                    if barcode.lower() == 'end':
                        break

                    found_item = None
                    for product in product_list:
                        if product.get_barcode() == barcode:
                            found_item = product
                            break

                    if found_item:
                        print(f"{found_item.get_name()}\n$ {found_item.get_price():.2f}")
                        checkout.scan_item(found_item)  # Subtract the item's price from payment due
                        while True:
                            another_item = input("Would you like to scan another item (Y/N): ").lower()
                            if another_item == 'n':
                                break
                            elif another_item != 'y':
                                print("Error - must enter Y or N")
                            else:
                                break  # Exit the loop if 'n' is entered

                        if another_item == 'n':
                            break  # Exit the loop if 'n' is entered

                    else:
                        print("ERROR - Scanned barcode is incorrect")
                        while True:
                            another_item = input("Would you like to scan another item (Y/N): ").lower()
                            if another_item == 'n':
                                break
                            elif another_item != 'y':
                                print("Error - must enter Y or N")
                            else:
                                break

                        if another_item == 'n':
                            break  # Exit the loop if 'n' is entered

                except ValueError:
                    print("Invalid barcode format")

            # Payment handling
            total_payment_due = checkout.get_total_payment()
            payment_received = 0
            while payment_received < total_payment_due:
                try:
                    payment = input(f"Payment due: ${total_payment_due - payment_received:.2f}. Enter payment amount: $")
                    payment = float(payment)  # Convert the input to a floating-point number

                    if payment < 0:
                        print("ERROR!! – Negative amounts are not accepted")
                    else:
                        payment_received += payment
                        if payment_received < total_payment_due:
                            print(f"Payment received: ${payment_received:.2f}. ${total_payment_due - payment_received:.2f} remaining.")
                        else:
                            break
                except ValueError:
                    print("Invalid input. Please enter a numeric amount.")

            # Calculate balance
            balance_given = payment_received - total_payment_due

            # Print receipt
            print("----- Final Receipt")
            for item in checkout.get_purchased_items():
                print(f"{item.get_name()}\n$ {item.get_price():.2f}")
            print(f"Total amount due: ${total_payment_due:.2f}")
            print(f"Amount received: ${payment_received:.2f}")
            print(f"Balance given: ${balance_given:.2f}")

            # Save the transaction details to transactions.txt with the current date and time, barcode, and price
            current_date = datetime.now().strftime("%d/%m/%Y")
            checkout.save_transaction(current_date, "transactions.txt")

            # Continue with another shopper?
            while True:
                continue_shopper = input("Continue with another shopper (Y/N): ").strip().lower()
                if continue_shopper == 'y':
                    break
                elif continue_shopper == 'n':
                    sys.exit("Thank you for shopping. Goodbye!")
                else:
                    print("Invalid input. Please enter Y or N.")

if __name__ == "__main__":
    main()
