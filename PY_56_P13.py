import tkinter as tk
from tkinter import messagebox

# Function to calculate energy bill based on the billing units
def calculate_bill():
    try:
        # Get the number of units from the entry box
        units = float(unit_entry.get())
        
        # If the input is a negative number - Additional activity
        if units < 0:
            messagebox.showerror("Error", "Units cannot be negative!")
            return
        
        # Energy bill calculation based on US standard
        if units <= 100:
            bill = units * 0.12
        elif units <= 300:
            bill = 100 * 0.12 + (units - 100) * 0.15
        else:
            bill = 100 * 0.12 + 200 * 0.15 + (units - 300) * 0.20
        
        # Display the result
        result_label.config(text=f"Energy Bill: ${bill:.2f}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of units!")

# Create the main window
root = tk.Tk()
root.title("Energy Billing Calculator")

# Create and place the labels, entries, and buttons in the window
unit_label = tk.Label(root, text="Enter Billing Units (kWh):")
unit_label.pack(pady=10)

unit_entry = tk.Entry(root)
unit_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Bill", command=calculate_bill)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Energy Bill: $0.00")
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
