import tkinter as tk
from tkinter import ttk

# Product list with prices
product_prices = {
    "Book": 10,
    "Toy": 15,
    "Snacks": 5,
    "Pencil": 2
}

def calculate_total():
    total = 0
    # Clear existing rows in the Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Add selected items to Treeview
    for item, var in cart_vars.items():
        if var.get():
            price = product_prices[item]
            total += price
            tree.insert('', 'end', values=(item, f"${price}"))

    result_label.config(text=f"💰 Total Amount: ${total}")

# GUI Setup
root = tk.Tk()
root.title("Shopping Cart Calculator 🛒")
root.geometry("400x400")

tk.Label(root, text="Select items to add to your cart:", font=("Arial", 12)).pack(pady=10)

# Checkbox dictionary
cart_vars = {}
for item, price in product_prices.items():
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=f"{item} (${price})", variable=var)
    cb.pack(anchor='w', padx=20)
    cart_vars[item] = var

# Button to calculate total
tk.Button(root, text="🧮 Calculate Total", command=calculate_total).pack(pady=10)

# Treeview for displaying selected items
tree = ttk.Treeview(root, columns=("Product", "Price"), show="headings", height=4)
tree.heading("Product", text="Product")
tree.heading("Price", text="Price")
tree.pack(pady=10)

# Label for total
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
