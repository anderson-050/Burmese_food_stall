# 🍜 Burmese Food Stall CLI Order System: Detailed Project Overview

#### Video Demo: <https://youtu.be/v0UIG7Fu4cg?si=SirKdxhRuU0fHx-1>

## 📝 Description and Rationale

This project is a **Command-Line Interface (CLI)** application written in Python that simulates the ordering process for a Burmese food stall. The primary goal is to provide a robust, interactive, and user-friendly experience that mimics real-world point-of-sale (POS) systems, but within a terminal environment. The application is designed not only to handle basic menu display and order taking but also to manage the subtle complexities of user input—like item naming variations—and efficient data processing, culminating in a clearly formatted, accurate final bill.

The rationale for this project centers on demonstrating proficiency in several core programming concepts: **data structure management** (handling the menu and the live order), **string manipulation and searching** (the flexible item matching), **input validation**, and **output formatting**. By focusing on a niche, culturally rich menu like Burmese cuisine, the project adds a unique and engaging flavor to an otherwise standard application. It's a practical example of how Python can be used for rapid development of utility applications.

-----

## ✨ Core Features Explained

### 1\. Interactive Menu Display

The application's starting point is a clean, easy-to-read menu. This is achieved by storing the food items and their prices in a suitable Python data structure (likely a dictionary or list of dictionaries) and then utilizing the **`tabulate`** library. This library is key to transforming raw data into a neatly aligned, **tabular format** that significantly enhances readability in the terminal.

### 2\. Flexible Item Matching (The Brain of the System) 🧠

This is arguably the most critical feature. The system anticipates that users may not type the exact, formal name of a menu item. It implements a flexible matching algorithm that checks user input against multiple data fields for each item:

  * **Full Item Name** (e.g., `"mohinga (fish noodle soup)"`)
  * **Main Item Name** (e.g., `"mohinga"`)
  * **Parenthesis Content/Description** (e.g., `"fish noodle soup"`)

All comparisons are **case-insensitive** and handle extra whitespace gracefully. For example, if the item is `"Laphet Thoke (Tea Leaf Salad)"` and a user types `"tea leaf salad"`, the system successfully matches it. This flexibility dramatically improves the user experience and reduces input errors.

### 3\. Quantity and Order Processing

Users can specify quantity directly in their input, typically separated by a comma (e.g., `"Tea Leaf Salad, 3"`). If no quantity is specified, the system **defaults to 1**.

### 4\. Order Consolidation

The application maintains a running order list. When a user orders an item that is **already in the current order**, the system doesn't create a new line item. Instead, it **updates the quantity** of the existing item and recalculates the subtotal. This ensures the final bill is concise and accurate, reflecting all purchases for a specific item on a single line.

-----

## Project Structure and Implementation Details

The project relies primarily on two main components within the `project.py` file:

### A. The Core Order Loop

The application runs in a **`while True`** loop, prompting the user for input. The input handling involves several steps:

1.  **Parsing:** Separating the item name string from the optional quantity string.
2.  **Matching:** Iterating through the `MENU` list and applying the flexible, case-insensitive logic to find a match.
3.  **Updating:** If a match is found, the **Order Consolidation** logic is applied to update the separate `current_order` data structure (e.g., a dictionary where keys are item names and values are the accumulated quantities).

### B. Bill Generation

When the user signals the end of the order, the final bill is generated. The system iterates through the consolidated order, performs the final calculations.

This information is then passed to the `tabulate` library with appropriate headers (Item, Qty, Unit Price, Total) to produce a professional, formatted bill.

-----

## 🔮 Future Enhancements

To evolve this simple system into a more feature-rich application, several extensions could be implemented:

  * **Customization Options:** Allow users to specify variations (e.g., "Mohinga with extra chili"). This would require an additional data structure to manage modifiers and their associated costs.
  * **Persistent Storage:** Instead of loading the menu statically, use **CSV or JSON files** to store the menu. This would allow the stall owner to easily update prices and items without changing the Python code.
  * **Receipt Output:** Implement a feature to save the final bill as a text file (`.txt`) or a simple markdown file, simulating a printed receipt.
  * **Error Reporting:** Provide more specific and helpful feedback to the user on invalid input (e.g., "Sorry, 'Khao' is too ambiguous. Did you mean 'Khao Sue' or 'Khao Pad'?").
  * **Discount/Tax Logic:** Introduce variables and functions to calculate sales tax or apply promotional discounts before determining the grand total.

-----

## Prerequisites

  * **`tabulate`**: Used for generating formatted tables (menu and bill).

### Installation

Install the required library using pip:

```bash
pip install tabulate
```

## Usage

  * use **`python`** to run this application

```bash
python project.py
```

  * use **`pytest`** to test this application

```bash
pytest project.py
```

-----
