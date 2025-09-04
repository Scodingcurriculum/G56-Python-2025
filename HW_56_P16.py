import tkinter as tk

# Food items and their calorie count (per unit)
food_items = {
    "Apple": 95,
    "Burger": 300,
    "Milk": 120,
    "Rice": 200,
    "Salad": 80
}

# Optional swaps for unhealthy items
healthier_swaps = {
    "Burger": "Grilled Veggie Wrap",
    "Rice": "Quinoa",
    "Milk": "Almond Milk"
}

# Function to calculate total and provide feedback
def calculate_meal():
    total = 0
    chosen = []

    for item, (var, entry) in inputs.items():
        if var.get():
            try:
                qty = int(entry.get())
            except ValueError:
                qty = 1   # default to 1 if blank/invalid
            total += food_items[item] * qty
            chosen.append(item)

    result = f"🍽️ Total Calories: {total} kcal\n"

    # Health feedback
    if total <= 400:
        result += "✅ This meal is Healthy!"
        color = "green"
    else:
        result += "⚠️ This meal is Not So Healthy."
        color = "red"

    # Suggest swaps
    suggestions = []
    for item in chosen:
        if item in healthier_swaps:
            suggestions.append(f"Swap {item} with {healthier_swaps[item]}")

    if suggestions:
        result += "\n\n🔄 Suggestions:\n" + "\n".join(suggestions)

    result_label.config(text=result, fg=color)


# GUI Setup
root = tk.Tk()
root.title("Healthy Meal Planner 🍽️ - Part 2")
root.geometry("400x450")

tk.Label(root, text="Select food items & quantity:", font=("Arial", 12)).pack(pady=10)

# Frame for food items
frame = tk.Frame(root)
frame.pack(pady=10)

# Dictionary to hold checkbutton variable + entry widget
inputs = {}

for item, cal in food_items.items():
    row = tk.Frame(frame)
    row.pack(anchor='w', pady=2)

    var = tk.BooleanVar()
    cb = tk.Checkbutton(row, text=f"{item} ({cal} kcal each)", variable=var)
    cb.pack(side='left')

    tk.Label(row, text="Qty:").pack(side='left', padx=5)
    qty_entry = tk.Entry(row, width=5)
    qty_entry.insert(0, "1")  # default quantity = 1
    qty_entry.pack(side='left')

    inputs[item] = (var, qty_entry)

# Button to calculate
tk.Button(root, text="Calculate Meal", command=calculate_meal).pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 10), justify="left", wraplength=350)
result_label.pack(pady=10)

root.mainloop()
