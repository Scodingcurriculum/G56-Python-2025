import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")  # Explicitly use the TkAgg backend

# Appliance data
appliances = ["TV", "Fridge", "Washing Machine", "Computer", "Fan", "AC", "Food Processor", "Microwave", "WiFi"]
wattage = {
    "TV": 100, "Fridge": 150, "Washing Machine": 500, "Computer": 200, "Fan": 75,
    "AC": 1500, "Food Processor": 300, "Microwave": 1200, "WiFi": 20
}
cost_per_kwh = 0.13

# Main window
root = tk.Tk()
root.title("💡 Energy Usage & Solar Savings Calculator")
root.geometry("1000x800")
root.configure(bg="#f0f9ff")

# Title
title = tk.Label(root, text="Grade 5-6 Energy Calculator", font=("Helvetica", 18, "bold"), bg="#f0f9ff", fg="#1d3557")
title.place(x=300, y=10)

# Frame for appliance inputs
input_frame = tk.LabelFrame(root, text="📋 Appliance Selection & Usage (hrs/day)", font=("Arial", 12, "bold"), bg="#e3f2fd", padx=10, pady=10)
input_frame.place(x=30, y=60, width=450, height=450)

selected_vars = {}
entries = {}

for i, app in enumerate(appliances):
    var = tk.IntVar()
    chk = tk.Checkbutton(input_frame, text=app, variable=var, bg="#e3f2fd", font=("Arial", 10))
    chk.place(x=10, y=10 + i * 40)

    ent = tk.Entry(input_frame, width=6, font=("Arial", 10))
    ent.place(x=200, y=10 + i * 40)
    ent.insert(0, "0")

    selected_vars[app] = var
    entries[app] = ent

# Calculate button
btn = tk.Button(root, text="🔍 Calculate", command=lambda: calculate(), bg="#00796b", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
btn.place(x=550, y=60)

# Treeview for appliance data
tree_frame = tk.LabelFrame(root, text="📊 Appliance-wise Energy & Cost", font=("Arial", 12, "bold"), bg="#f0f9ff")
tree_frame.place(x=500, y=110, width=460, height=250)

tree = ttk.Treeview(tree_frame, columns=("Appliance", "Usage", "Energy", "Cost"), show="headings", height=9)
tree.heading("Appliance", text="Appliance")
tree.heading("Usage", text="Usage (hrs/day)")
tree.heading("Energy", text="Energy (kWh/day)")
tree.heading("Cost", text="Cost ($/day)")

tree.column("Appliance", width=100)
tree.column("Usage", width=100)
tree.column("Energy", width=120)
tree.column("Cost", width=100)
tree.place(x=0, y=0, width=445, height=220)

# Scrollbar for treeview (optional if needed)
tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=tree_scroll.set)
tree_scroll.place(x=445, y=0, height=220)

# Summary frame
result_frame = tk.LabelFrame(root, text="📈 Summary & Suggestions", font=("Arial", 12, "bold"), bg="#f0f9ff")
result_frame.place(x=30, y=530, width=930, height=230)

# Scrollable text area
text_frame = tk.Frame(result_frame, bg="white")
text_frame.place(x=10, y=10, width=900, height=190)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side='right', fill='y')

output_text = tk.Text(text_frame, font=("Arial", 11), yscrollcommand=scrollbar.set, wrap='word')
output_text.pack(side='left', fill='both', expand=True)
scrollbar.config(command=output_text.yview)

def calculate():
    tree.delete(*tree.get_children())
    output_text.delete("1.0", tk.END) # Clear previous table content

    total_energy = 0
    total_cost = 0

    output_text.insert(tk.END, "Energy and Cost Summary:\n\n")

    for appliance in appliances:
        if selected_vars[appliance].get() == 1:
            try:
                usage_hours = float(entries[appliance].get())  
                # Get usage for the current appliance
                
                energy_consumed = round((wattage[appliance] * usage_hours) / 1000, 2)  
                # Calculate energy consumed (in kWh)
                
                cost = round(energy_consumed * cost_per_kwh, 2)  
                # Calculate cost (USD)

                total_energy += energy_consumed  # Add to total energy
                total_cost += cost  # Add to total cost

                # Insert into treeview
                tree.insert("", "end", values=(appliance, f"{usage_hours[app]} hrs", f"{energy_consumed[app]} kWh", f"${cost[app]:.2f}"))

                # Summary for the appliance
                output_text.insert(tk.END, f"🔌 {appliance}: Used for {usage_hours[app]} hrs → {energy_consumed[app]} kWh → Cost: ${cost[app]:.2f}\n")


            except ValueError:
                output_text.insert(tk.END, f"{appliance}: Invalid input.\n")

    # Insert total energy and cost
    output_text.insert(tk.END, f"\nTotal Energy: {total_energy:.2f} kWh\n")
    output_text.insert(tk.END, f"Total Cost: ${total_cost:.2f}")

root.mainloop()
