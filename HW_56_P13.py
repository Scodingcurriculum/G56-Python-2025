import tkinter as tk
from tkinter import ttk

# Optional: Basic color name matching
def get_color_name(hex_code):
    basic_colors = {
        '#000000': 'Black',
        '#FFFFFF': 'White',
        '#FF0000': 'Red',
        '#00FF00': 'Green',
        '#0000FF': 'Blue',
        '#FFFF00': 'Yellow',
        '#00FFFF': 'Cyan',
        '#FF00FF': 'Magenta',
        '#808080': 'Gray',
    }
    return basic_colors.get(hex_code.upper(), 'Unknown')

# Update color preview and hex code
def update_color(event=None):
    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()
    
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    
    color_box.config(bg=hex_color)
    hex_label.config(text=f"Hex Code: {hex_color.upper()}")
    name_label.config(text=f"Color Name: {get_color_name(hex_color)}")

# Main Window
root = tk.Tk()
root.title("🎨 RGB Color Mixer")

# Sliders for RGB
red_slider = ttk.Scale(root, from_=0, to=255, orient='horizontal', command=update_color)
green_slider = ttk.Scale(root, from_=0, to=255, orient='horizontal', command=update_color)
blue_slider = ttk.Scale(root, from_=0, to=255, orient='horizontal', command=update_color)

# Labels
tk.Label(root, text="Red").pack()
red_slider.pack(fill='x', padx=20)

tk.Label(root, text="Green").pack()
green_slider.pack(fill='x', padx=20)

tk.Label(root, text="Blue").pack()
blue_slider.pack(fill='x', padx=20)

# Color preview box
color_box = tk.Label(root, text=" Color Preview ", bg="#000000", width=30, height=5)
color_box.pack(pady=10)

# Hex and Name display
hex_label = tk.Label(root, text="Hex Code: #000000")
hex_label.pack()
name_label = tk.Label(root, text="Color Name: Black")
name_label.pack()

# Start with black
update_color()

# Run the app
root.mainloop()
