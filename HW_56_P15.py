import tkinter as tk
from tkinter import ttk

# Country data dictionary
# Format: country: [capital, currency, language, continent]
country_data = {
    "India": ["New Delhi", "Indian Rupee", "Hindi, English", "Asia"],
    "France": ["Paris", "Euro", "French", "Europe"],
    "Japan": ["Tokyo", "Yen", "Japanese", "Asia"],
    "USA": ["Washington, D.C.", "US Dollar", "English", "North America"],
    "Brazil": ["Brasília", "Brazilian Real", "Portuguese", "South America"],
    "Egypt": ["Cairo", "Egyptian Pound", "Arabic", "Africa"]
}

# Update labels based on country selection
def show_info(event):
    country = selected_country.get()
    if country in country_data:
        capital, currency, language, continent = country_data[country]
        capital_label.config(text=f"Capital: {capital}")
        currency_label.config(text=f"Currency: {currency}")
        language_label.config(text=f"Language: {language}")
        continent_label.config(text=f"Continent: {continent}")

# GUI setup
root = tk.Tk()
root.title("Country Info App 🌍")
root.geometry("350x250")

tk.Label(root, text="Select a Country:", font=("Arial", 12)).pack(pady=10)

selected_country = tk.StringVar()
country_menu = ttk.Combobox(root, textvariable=selected_country, values=list(country_data.keys()), state="readonly")
country_menu.pack()
country_menu.bind("<<ComboboxSelected>>", show_info)

# Info labels
capital_label = tk.Label(root, text="Capital: ", font=("Arial", 10))
capital_label.pack(pady=5)

currency_label = tk.Label(root, text="Currency: ", font=("Arial", 10))
currency_label.pack(pady=5)

language_label = tk.Label(root, text="Language: ", font=("Arial", 10))
language_label.pack(pady=5)

continent_label = tk.Label(root, text="Continent: ", font=("Arial", 10))
continent_label.pack(pady=5)

root.mainloop()
