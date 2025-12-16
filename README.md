# 🍜 Burmese Food Stall CLI Order System

A robust and interactive **Command-Line Interface (CLI)** application written in Python that simulates the ordering process for a Burmese food stall. This system is designed to provide a user-friendly experience that mimics real-world point-of-sale (POS) systems within a terminal environment.

#### [Video Demo](https://youtu.be/v0UIG7Fu4cg?si=ynD-tremFAbITot6)

## 📝 Project Overview

This Python CLI application efficiently handles the complexities of taking food orders, from displaying a clean menu to processing flexible user input and generating an accurate bill. It demonstrates core programming concepts like data structure management, string manipulation for flexible item matching, and professional output formatting. By focusing on a culturally rich menu, the project offers a unique and practical utility application.

## ✨ Core Features

  * **Interactive Menu Display:** The system utilizes the **`tabulate`** library to transform raw menu data into a neat, easily readable tabular format directly in the terminal.
  * **Flexible Item Matching (The Brain of the System) 🧠:** This critical feature allows the system to anticipate variations in user input. It performs **case-insensitive** matching against the:
      * Full Item Name (e.g., "Laphet Thoke (Tea Leaf Salad)")
      * Main Item Name (e.g., "Laphet Thoke")
      * Parenthesis Content/Description (e.g., "Tea Leaf Salad")
  * **Quantity and Order Processing:** Users can specify quantity (e.g., `"Khao Sue, 3"`); if omitted, the system defaults the quantity to 1.
  * **Order Consolidation:** The application maintains a running order and automatically **updates the quantity** of an existing item instead of creating a new line item, ensuring the final bill is concise and accurate.
  * **Bill Generation:** Produces a professional final bill with clear columns for Item, Quantity, Unit Price, and Total, leveraging the `tabulate` library for alignment.

### 🔮 Future Enhancements

To evolve this system into a more feature-rich application, the following extensions are planned:

  * **Customization Options:** Allow users to specify variations (e.g., "Mohinga with extra chili").
  * **Persistent Storage:** Use **CSV or JSON files** to store the menu, allowing the stall owner to easily update prices and items without changing the Python code.
  * **Receipt Output:** Implement a feature to save the final bill as a text file (`.txt`) or a simple markdown file, simulating a printed receipt.
  * **Error Reporting:** Provide more specific feedback on invalid input (e.g., suggesting item names when input is ambiguous).
  * **Discount/Tax Logic:** Introduce variables and functions to calculate sales tax or apply promotional discounts before determining the grand total.

## 🛠️ Prerequisites

  * **Python 3**
  * **`tabulate`**: Used for generating formatted tables (menu and bill).

### Installation

Install the required library using pip:

```bash
pip install tabulate
```

## 🚀 How to Use

Run the application from your terminal:

```bash
python project.py
```

To run the integrated tests:

```bash
pytest project.py
```

## License

#### [MIT](LICENSE)
