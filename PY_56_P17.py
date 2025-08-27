import tkinter as tk
from tkinter import ttk

# Dictionary storing appliances and their wattages
appliance_wattage = {
    "TV": 100,
    "Fridge": 150,
    "Washing Machine": 500,
    "Computer": 200,
    "Fan": 75
}

# Hardcoded average U.S. electricity rate in USD per kWh
electricity_rate = 0.13  # in USD/kWh

root = tk.Tk()
root.title("Energy Usage Calculator")
root.geometry("800x600")

appliances = list(appliance_wattage.keys())
selected_vars = {}
hour_entries = {}

# --- Title ---
title_label = tk.Label(root, text="Appliance Energy Usage Calculator", font=("Helvetica", 16, "bold"))
title_label.place(x=230, y=10)

# --- Frame for selecting appliances and hours ---
input_frame = tk.LabelFrame(root, text="Select Appliances & Usage", padx=10, pady=10)
input_frame.place(x=20, y=50, width=760, height=200)

# Add checkbox and hour entry for each appliance
for i, appliance in enumerate(appliances):
    var = tk.IntVar()
    chk = tk.Checkbutton(input_frame, text=appliance, variable=var)
    chk.grid(row=i, column=0, sticky='w')

    hour_label = tk.Label(input_frame, text="Hours/Day:")
    hour_label.grid(row=i, column=1)

    entry = tk.Entry(input_frame, width=5)
    entry.grid(row=i, column=2)

    selected_vars[appliance] = var
    hour_entries[appliance] = entry

# --- NEW: Treeview Table to show calculation results ---
table_frame = tk.LabelFrame(root, text="Appliance-wise Energy & Cost")
table_frame.place(x=20, y=300, width=760, height=200)

tree = ttk.Treeview(table_frame, columns=("Appliance", "Hours", "kWh", "Cost"), show="headings")
tree.heading("Appliance", text="Appliance")
tree.heading("Hours", text="Hours/Day")
tree.heading("kWh", text="Energy (kWh)")
tree.heading("Cost", text="Cost (USD)")

tree.column("Appliance", width=150)
tree.column("Hours", width=100)
tree.column("kWh", width=120)
tree.column("Cost", width=100)

tree.pack(fill='both', expand=True)

# --- Output Box with Scrollbar ---
output_frame = tk.Frame(root)
output_frame.place(x=20, y=510, width=760, height=70)

scrollbar = tk.Scrollbar(output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(output_frame, height=4, yscrollcommand=scrollbar.set, wrap='word')
output_text.pack(fill='both', expand=True)
scrollbar.config(command=output_text.yview)

# --- Calculate Button ---
def calculate():
    output_text.delete("1.0", tk.END)
    tree.delete(*tree.get_children())  # Clear previous table content

    total_energy = 0
    total_cost = 0

    output_text.insert(tk.END, "Energy and Cost Summary:\n\n")

    for appliance in appliances:
        if selected_vars[appliance].get() == 1:
            try:
                hours = float(hour_entries[appliance].get())
                watt = appliance_wattage[appliance]
                energy_kwh = (watt * hours) / 1000  # kWh = (Watt × Hours) / 1000
                cost = energy_kwh * electricity_rate  # Cost = Energy (kWh) × Rate (USD/kWh)

                total_energy += energy_kwh
                total_cost += cost

                # Show in table
                tree.insert('', 'end', values=(appliance, hours, f"{energy_kwh:.2f}", f"${cost:.2f}"))

                # Summary
                output_text.insert(tk.END, f"{appliance}: {energy_kwh:.2f} kWh × ${electricity_rate:.2f} = ${cost:.2f}\n")
            except ValueError:
                output_text.insert(tk.END, f"{appliance}: Invalid input.\n")

    output_text.insert(tk.END, f"\nTotal Energy: {total_energy:.2f} kWh\n")
    output_text.insert(tk.END, f"Total Cost: ${total_cost:.2f}")

# Button to trigger calculation
calc_btn = tk.Button(root, text="Calculate", command=calculate)
calc_btn.place(x=650, y=260)

root.mainloop()
