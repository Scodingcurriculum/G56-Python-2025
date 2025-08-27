import tkinter as tk
import matplotlib.pyplot as plt

# Function to calculate profit or loss and visualize the results
def calculate_profit_loss():
    try:
        # Get the input values from the user
        sold_ballpoint = int(entry_sold_ballpoint.get())  # Ballpoint pens sold
        sold_ink = int(entry_sold_ink.get())  # Ink pens sold
        sold_gel = int(entry_sold_gel.get())  # Gel pens sold
        
        cost_ballpoint = 3.00  # Cost price for Ballpoint pen
        selling_ballpoint = float(entry_selling_ballpoint.get())  # Selling price for Ballpoint pen
        
        cost_ink = 10.00  # Cost price for Ink pen
        selling_ink = float(entry_selling_ink.get())  # Selling price for Ink pen
        
        cost_gel = 6.00  # Cost price for Gel pen
        selling_gel = float(entry_selling_gel.get())  # Selling price for Gel pen
        
        # Calculating profit or loss for each type of pen
        profit_loss_ballpoint = (selling_ballpoint - cost_ballpoint) * sold_ballpoint
        profit_loss_ink = (selling_ink - cost_ink) * sold_ink
        profit_loss_gel = (selling_gel - cost_gel) * sold_gel
        
        # Display the profit/loss for each type of pen
        result_label.config(
            text=f"📊 Profit/Loss for each pen type:\n\n"
                 f"✒️ Ballpoint Pens: {'Profit' if profit_loss_ballpoint >= 0 else 'Loss'} = ${profit_loss_ballpoint:.2f}\n"
                 f"🖊️ Ink Pens: {'Profit' if profit_loss_ink >= 0 else 'Loss'} = ${profit_loss_ink:.2f}\n"
                 f"✍️ Gel Pens: {'Profit' if profit_loss_gel >= 0 else 'Loss'} = ${profit_loss_gel:.2f}\n\n"
        )
        
        # Calculate total profit or loss
        total_profit_loss = profit_loss_ballpoint + profit_loss_ink + profit_loss_gel
        total_label.config(
            text=f"💰 Total Profit/Loss: ${total_profit_loss:.2f}"
        )
        
        # Call function to visualize the profit/loss as a bar chart
        visualize_profit_loss(profit_loss_ballpoint, profit_loss_ink, profit_loss_gel, total_profit_loss)
        
    except ValueError:
        result_label.config(text="❌ Please enter valid numbers for all fields!")

# Function to create a bar chart visualizing the profit/loss
def visualize_profit_loss(ballpoint, ink, gel, total):
    categories = ['Ballpoint', 'Ink', 'Gel', 'Total']
    profits = [ballpoint, ink, gel, total]
    
    plt.figure(figsize=(6, 4))
    plt.bar(categories, profits, color=['blue', 'green', 'red', 'purple'])
    plt.title("Profit/Loss Visualization")
    plt.ylabel("Profit/Loss ($)")
    plt.show()

# Create the Tkinter window
root = tk.Tk()
root.title("Pen Sales Tracker")
root.geometry("500x600")
root.configure(bg="#f0f8ff")

# Title label
tk.Label(root, text="🖊️ Pen Sales Tracker", font=("Helvetica", 16, "bold"), bg="#f0f8ff").place(x=150, y=10)

# Input fields for pens sold
tk.Label(root, text="Ballpoint Pens Sold:", bg="#f0f8ff").place(x=30, y=60)
entry_sold_ballpoint = tk.Entry(root)
entry_sold_ballpoint.place(x=220, y=60)

tk.Label(root, text="Ink Pens Sold:", bg="#f0f8ff").place(x=30, y=90)
entry_sold_ink = tk.Entry(root)
entry_sold_ink.place(x=220, y=90)

tk.Label(root, text="Gel Pens Sold:", bg="#f0f8ff").place(x=30, y=120)
entry_sold_gel = tk.Entry(root)
entry_sold_gel.place(x=220, y=120)

tk.Label(root, text="Selling Price of Ballpoint Pen ($):", bg="#f0f8ff").place(x=30, y=190)
entry_selling_ballpoint = tk.Entry(root)
entry_selling_ballpoint.place(x=220, y=190)

tk.Label(root, text="Selling Price of Ink Pen ($):", bg="#f0f8ff").place(x=30, y=250)
entry_selling_ink = tk.Entry(root)
entry_selling_ink.place(x=220, y=250)

tk.Label(root, text="Selling Price of Gel Pen ($):", bg="#f0f8ff").place(x=30, y=310)
entry_selling_gel = tk.Entry(root)
entry_selling_gel.place(x=220, y=310)

# Button to calculate profit/loss
tk.Button(root, text="⚡ Calculate Profit/Loss", font=("Arial", 12), bg="#007acc", fg="white", command=calculate_profit_loss).place(x=150, y=350)

# Result label (displays profit/loss for each pen type)
result_label = tk.Label(root, text="", font=("Arial", 11), justify="left", bg="#f0f8ff", fg="#333")
result_label.place(x=40, y=400)

# Total profit/loss label
total_label = tk.Label(root, text="", font=("Arial", 11), justify="left", bg="#f0f8ff", fg="#333")
total_label.place(x=40, y=450)

# Start the Tkinter event loop
root.mainloop()
