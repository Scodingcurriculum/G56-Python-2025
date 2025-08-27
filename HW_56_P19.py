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
    # Clear previous entries
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
root.geometry("500x450")
root.config(bg="#f0f4f7")

# Title
title = tk.Label(root, text="🛒 Shopping Cart", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333")
title.place(x=150, y=20)

# Instructions
instructions = tk.Label(root, text="Select items to add to your cart:", font=("Helvetica", 12), bg="#f0f4f7", fg="#444")
instructions.place(x=40, y=70)

# Checkboxes with place
cart_vars = {}
y_pos = 100
for item, price in product_prices.items():
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=f"{item} (${price})", font=("Arial", 11), bg="#f0f4f7", variable=var)
    cb.place(x=60, y=y_pos)
    cart_vars[item] = var
    y_pos += 30

# Calculate Button
calc_btn = tk.Button(root, text="🧮 Calculate Total", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=calculate_total)
calc_btn.place(x=160, y=230)

# Treeview to display items
tree = ttk.Treeview(root, columns=("Product", "Price"), show="headings", height=4)
tree.heading("Product", text="Product")
tree.heading("Price", text="Price")
tree.place(x=90, y=280)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), fg="#d35400", bg="#f0f4f7")
result_label.place(x=150, y=370)

root.mainloop()
