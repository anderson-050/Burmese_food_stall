import re
from tabulate import tabulate

def get_menu():
    return [
        {"Item": "Mohinga (Fish Noodle Soup)", "Price": "$1.50"},
        {"Item": "Laphet Thoke (Tea Leaf Salad)", "Price": "$1.20"},
        {"Item": "Shan Khao Swe (Shan Noodles)", "Price": "$1.80"},
        {"Item": "E Kya Kway (Fried Dough Stick)", "Price": "$0.80"},
        {"Item": "Burmese Milk Tea", "Price": "$0.50"},
    ]

def display_menu(menu):
    print("\n--- Welcome to the Burmese Food Stall! ---")
    print(tabulate(menu, headers="keys", tablefmt="rounded_outline"))
    print("-" * 43)

def item_match(item_input, menu):
    for item in menu:
        item_name = item["Item"]
        price_str = item["Price"]

        #1. Full name match
        if item_name.lower() == item_input:
            return item_name, price_str

        #2. Main name match
        main_name = item_name.split("(")[0].strip().lower()
        if main_name == item_input:
            return item_name, price_str

        #3. Parenthesis content match
        if match := re.search(r"\((.*?)\)", item_name):
            if match.group(1).lower() == item_input:
                return item_name, price_str

    return None

def get_item_data(item_input, menu):
    match_data = item_match(item_input, menu)
    if match_data:
        return match_data[0], float(match_data[1].replace("$", "").strip())
    return None

def process_order(menu):
    order_list = []

    print("\n--- Order Instructions ---")
    print("*Enter a item you want to order and its quantity (e.g., Mohinga, 2)")
    print("*Type 'Exit' or 'E' to finish ordering and get your bill\n")

    while True:
        try:
            choice = input("Order: ").strip().lower()
        except EOFError:
            break

        if choice in ["e", "exit", "no"]:
            break

        parts = [p.strip() for p in choice.split(",")]

        item_input = None
        quantity = 1

        if len(parts) == 0:
            continue
        elif len(parts) == 1:
            item_input = parts[0]
            quantity = 1
        elif len(parts) == 2:
            item_input = parts[0]
            quantity = parts[1]
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    print("Invalid quantity")
                    continue
            except ValueError:
                print("Invalid quantity")
                continue
        else:
            print("Invalid order format")
            continue

        item_data = get_item_data(item_input, menu)
        if item_data:
            full_name, unit_price = item_data
            total_item_price = unit_price * quantity

            # Consolidation logic: Check if item already exists
            existing_item = next((item for item in order_list if item["Item"] == full_name), None)

            if existing_item:
                existing_item["Quantity"] += quantity
                existing_item["Total Price"] += total_item_price
            else:
                order_list.append({
                    "Item": full_name,
                    "Quantity": quantity,
                    "Price": unit_price,
                    "Total Price": total_item_price
                })

            print(f"Successfully added {quantity} x '{full_name}'\nWhat else do you want? ", end="")

        else:
            #Item match not found
            print("This item is not available")

    return order_list

def generate_bill_table(order_list):
    if not order_list:
        return 0.0, ""
        # final_total, bill_text

    bill_data = []
    for item in order_list:
        bill_data.append({
            "Item": item["Item"],
            "Qty": item["Quantity"],
            "Unit Price": f"${item['Price']:.2f}",
            "Amount": f"${item['Total Price']:.2f}"
        })

    # sum(x for x in list)
    final_total = sum(item["Total Price"] for item in order_list)

    table = tabulate(bill_data, headers="keys", tablefmt="rounded_outline")

    bill_output = [
        "\n" + "-" * 25 + "--- B I L L ---" + "-" * 25,
        table,
        f"Total: ${final_total:.2f}",
        "-" * 65
    ]

    return final_total, "\n".join(bill_output)

def main():
    menu = get_menu()
    display_menu(menu)

    order_list = process_order(menu)

    final_total, bill_text = generate_bill_table(order_list)

    if final_total > 0:
        print(bill_text)
    print("Thanks for visiting us. Have a nice day!")

if __name__ == "__main__":
    main()
