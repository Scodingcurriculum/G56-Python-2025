import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.title("Energy Usage Calculator")
root.geometry("700x500")

# Title
title = tk.Label(root, text="Appliance Energy Usage", font=("Helvetica", 16))
title.pack(pady=10)

# Input Frame for selecting appliances and hours
input_frame = tk.LabelFrame(root, text="Select Appliances and Enter Usage (hrs/day)", padx=10, pady=10)
input_frame.pack(pady=10, fill='x')

# List of appliances
appliances = ["TV", "Fridge", "Washing Machine", "Computer", "Fan"]

selected_vars = {}
hour_entries = {}

# Creating Checkbuttons and Entry for each appliance
for i, appliance in enumerate(appliances):
    var = tk.IntVar()
    chk = tk.Checkbutton(input_frame, text=appliance, variable=var)
    chk.grid(row=i, column=0, sticky='w', padx=10)

    hour_label = tk.Label(input_frame, text="Hours:")
    hour_label.grid(row=i, column=1, padx=5)
    
    entry = tk.Entry(input_frame, width=5)
    entry.grid(row=i, column=2)

    selected_vars[appliance] = var
    hour_entries[appliance] = entry

# Calculate function
def calculate():
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Selected Appliances & Hours:\n\n")
    for appliance in appliances:
        if selected_vars[appliance].get() == 1:
            hours = hour_entries[appliance].get()
            if hours:
                output_text.insert(tk.END, f"{appliance}: {hours} hrs/day\n")
            else:
                output_text.insert(tk.END, f"{appliance}: No hours entered\n")

# Calculate Button
calc_btn = tk.Button(root, text="Calculate", command=calculate)
calc_btn.pack(pady=10)

# Scrollable Text area for summary
summary_frame = tk.Frame(root)
summary_frame.pack(padx=10, pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(summary_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text = tk.Text(summary_frame, height=10, yscrollcommand=scrollbar.set, wrap='word')
output_text.pack(fill="both", expand=True)

scrollbar.config(command=output_text.yview)

# Start app
root.mainloop()
