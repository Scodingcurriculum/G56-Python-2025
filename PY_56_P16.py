import tkinter as tk
from tkinter import ttk

# --- Class 15: Define wattage for each appliance ---
appliance_wattage = {
    "TV": 100,                 # in watts
    "Fridge": 150,
    "Washing Machine": 500,
    "Computer": 200,
    "Fan": 75
}

# --- Base Setup ---
root = tk.Tk()
root.title("Energy Usage Calculator")
root.geometry("700x550")

appliances = list(appliance_wattage.keys())  # List of appliance names
selected_vars = {}   # Stores IntVar for each checkbox
hour_entries = {}    # Stores Entry widget for each appliance

# --- GUI Title ---
title = tk.Label(root, text="Appliance Energy Usage", font=("Helvetica", 16))
title.pack(pady=10)

# --- Input Frame (Checkbox + Hours Input) ---
input_frame = tk.LabelFrame(root, text="Select Appliances and Enter Usage (hrs/day)", padx=10, pady=10)
input_frame.pack(pady=10, fill='x')

for i, appliance in enumerate(appliances):
    # --- Class 13-14 code: Checkboxes and entry fields ---
    var = tk.IntVar()
    chk = tk.Checkbutton(input_frame, text=appliance, variable=var)
    chk.grid(row=i, column=0, sticky='w', padx=10)

    hour_label = tk.Label(input_frame, text="Hours:")
    hour_label.grid(row=i, column=1, padx=5)

    entry = tk.Entry(input_frame, width=5)
    entry.grid(row=i, column=2)

    selected_vars[appliance] = var
    hour_entries[appliance] = entry

# --- Class 16: Function to calculate energy usage ---
def calculate():
    output_text.delete("1.0", tk.END)  # Clear previous output
    output_text.insert(tk.END, "Appliance-wise Energy Usage:\n\n")

    total_energy = 0  # Initialize total energy variable

    for appliance in appliances:
        if selected_vars[appliance].get() == 1:  # If checkbox is selected
            try:
                hours = float(hour_entries[appliance].get())  # Get entered hours
                watt = appliance_wattage[appliance]           # Get wattage
                energy_kwh = (watt * hours) / 1000            # Convert to kWh
                total_energy += energy_kwh
                output_text.insert(tk.END, f"{appliance}: {hours} hrs × {watt}W = {energy_kwh:.2f} kWh/day\n")
            except ValueError:
                output_text.insert(tk.END, f"{appliance}: Invalid hours input!\n")

    output_text.insert(tk.END, f"\nTotal Energy Used Per Day: {total_energy:.2f} kWh")

# --- Calculate Button ---
calc_btn = tk.Button(root, text="Calculate", command=calculate)
calc_btn.pack(pady=10)

# --- Class 15: Scrollable Text Summary Output ---
summary_frame = tk.Frame(root)
summary_frame.pack(padx=10, pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(summary_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(summary_frame, height=10, yscrollcommand=scrollbar.set, wrap='word')
output_text.pack(fill="both", expand=True)

scrollbar.config(command=output_text.yview)

# --- Run App ---
root.mainloop()
