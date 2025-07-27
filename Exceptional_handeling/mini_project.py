# 1. Purchase

def process_purchase_file():
    try:
        filename = input("Enter the file name: ") + ".txt"

        with open(filename, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        items_purchased = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            parts = line.split()

            if len(parts) == 2:
                name, value = parts[0], parts[1]

                if value.lower() == "free":
                    free_items += 1
                elif name.lower() == "discount":
                    discount = int(value)
                else:
                    total_amount += int(value)
                    items_purchased += 1

        final_amount = total_amount - discount

        print(f"No of items purchased: {items_purchased}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid data in file (non-numeric price or discount).")
    except Exception as e:
        print("Error:", e)

process_purchase_file()
