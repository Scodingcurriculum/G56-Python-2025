import tkinter as tk

# Food items and their calorie count
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

    for item, var in checkboxes.items():
        if var.get():
            total += food_items[item]
            chosen.append(item)

    result = f"🍽️ Total Calories: {total} kcal\n"

    # Health feedback
    if total <= 400:
        result += "✅ This meal is Healthy!"
    else:
        result += "⚠️ This meal is Not So Healthy."

    # Suggest swaps
    suggestions = []
    for item in chosen:
        if item in healthier_swaps:
            suggestions.append(f"Swap {item} with {healthier_swaps[item]}")

    if suggestions:
        result += "\n\n🔄 Suggestions:\n" + "\n".join(suggestions)

    result_label.config(text=result)

# GUI Setup
root = tk.Tk()
root.title("Healthy Meal Planner 🍽️")
root.geometry("350x400")

tk.Label(root, text="Select food items for your meal:", font=("Arial", 12)).pack(pady=10)

# Checkboxes for items
checkboxes = {}
for item in food_items:
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=f"{item} ({food_items[item]} kcal)", variable=var)
    cb.pack(anchor='w', padx=20)
    checkboxes[item] = var

# Button to calculate
tk.Button(root, text="Calculate Meal", command=calculate_meal).pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
result_label.pack(pady=10)

root.mainloop()
