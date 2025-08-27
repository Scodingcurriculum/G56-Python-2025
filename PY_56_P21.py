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

result_textbox = tk.Text(text_frame, font=("Arial", 11), yscrollcommand=scrollbar.set, wrap='word')
result_textbox.pack(side='left', fill='both', expand=True)
scrollbar.config(command=result_textbox.yview)

# Calculation logic
def calculate():
    tree.delete(*tree.get_children())
    result_textbox.delete("1.0", tk.END)

    selected_appliances = [app for app in appliances if selected_vars[app].get() == 1]
    if not selected_appliances:
        messagebox.showwarning("No Appliance Selected", "Please select at least one appliance.")
        return

    try:
        usage_hours = {app: float(entries[app].get()) for app in selected_appliances}
        energy_consumed = {app: round((wattage[app] * usage_hours[app]) / 1000, 2) for app in selected_appliances}
        cost = {app: round(energy_consumed[app] * cost_per_kwh, 2) for app in selected_appliances}

        daily = round(sum(energy_consumed.values()), 2)
        monthly = round(daily * 30, 2)
        yearly = round(daily * 365, 2)

        suggested_panels = round(daily / 1.5)
        solar_energy = round(suggested_panels * 1.5, 2)

        saved_kwh = min(daily, solar_energy)
        saved_money = round(saved_kwh * cost_per_kwh, 2)

        panel_cost = 250
        install_cost = 500
        total_cost = panel_cost * suggested_panels + install_cost
        break_even = round(total_cost / saved_money, 1) if saved_money > 0 else "-"

        for app in selected_appliances:
            tree.insert("", "end", values=(app, usage_hours[app], energy_consumed[app], f"${cost[app]:.2f}"))

        result_text = f"""
📌 Daily Energy Usage: {daily} kWh
🔋 Solar Energy Generated (Suggested Panels = {suggested_panels}): {solar_energy} kWh
____________________________________________________________________________________

✅ Savings if Solar is Used:
- Daily Savings: {saved_kwh} kWh | ${saved_money}
- Monthly Savings: {round(saved_kwh * 30, 2)} kWh | ${round(saved_money * 30, 2)}
- Yearly Savings: {round(saved_kwh * 365, 2)} kWh | ${round(saved_money * 365, 2)}
____________________________________________________________________________________
💰 Break-even Time: {break_even} days
💸 Total Solar Setup Cost: ${total_cost}
        """
        result_textbox.insert(tk.END, result_text)

        # Plot
                 # Plot: Yearly cost vs solar savings per appliance
        labels = selected_appliances
        yearly_costs = [round(cost[app] * 365, 2) for app in labels]

        # Distribute solar energy per appliance (proportionally)
        total_energy = sum(energy_consumed.values())
        solar_energy_share = {app: (energy_consumed[app] / total_energy) * solar_energy if total_energy > 0 else 0 for app in labels}
        solar_savings = [round(min(energy_consumed[app], solar_energy_share[app]) * cost_per_kwh * 365, 2) for app in labels]

        net_cost = [round(yearly_costs[i] - solar_savings[i], 2) for i in range(len(labels))]

        plt.figure(figsize=(10, 6))
        x = range(len(labels))
        bar_width = 0.35

        plt.bar(x, yearly_costs, width=bar_width, label='Yearly Electricity Cost ($)', color='salmon')
        plt.bar([i + bar_width for i in x], net_cost, width=bar_width, label='Cost After Solar Savings ($)', color='mediumseagreen')

        plt.xlabel("Appliance")
        plt.ylabel("Yearly Cost ($)")
        plt.title("Yearly Cost: Electricity vs Solar Offset")
        plt.xticks([i + bar_width / 2 for i in x], labels, rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.grid(axis='y')
        plt.show()


    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all usage fields.")

root.mainloop()
