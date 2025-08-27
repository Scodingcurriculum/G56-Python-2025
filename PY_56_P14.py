import tkinter as tk

# Main window setup
root = tk.Tk()
root.title("Energy Usage Calculator")
root.geometry("600x400")

# Introduction label
title = tk.Label(root, text="Appliance Energy Usage", font=("Helvetica", 16))
title.pack(pady=20)

# Input frame for appliance selection
input_frame = tk.LabelFrame(root, text="Select Appliances", font=("Arial", 12), padx=10, pady=10)
input_frame.pack(pady=10)

# List of appliances
appliances = ["TV", "Fridge", "Washing Machine", "Computer", "Fan"]

# Checkbuttons for each appliance
selected_vars = {}
for appliance in appliances:
    var = tk.IntVar()
    chk = tk.Checkbutton(input_frame, text=appliance, variable=var)
    chk.pack(anchor='w')
    selected_vars[appliance] = var

# Output label to display the selected appliances
result_label = tk.Label(root, text="Appliance Usage will appear here.", font=("Arial", 12))
result_label.pack(pady=20)

# Calculate function
def calculate():
    selected_appliances = [app for app, var in selected_vars.items() if var.get() == 1]
    if selected_appliances:
        result_label.config(text=f"Selected Appliances: {', '.join(selected_appliances)}")
    else:
        result_label.config(text="No appliances selected.")

# Calculate button
btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack(pady=10)

# Start the application
root.mainloop()
