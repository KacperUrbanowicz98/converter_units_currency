import tkinter as tk
from tkinter import ttk

#Main windows
window = tk.Tk()
window.title("Konwerter jednostek i walut")
window.geometry("400x400")

mode = tk.StringVar(value="units")

label_mode = tk.Label(window, text="Wybierz tryb: ", font=("Arial", 12, "bold"))
label_mode.pack(pady=10)

radio_units = tk.Radiobutton(window, text="Jednostki miary", variable=mode, value="units")
radio_units.pack()

radio_currency = tk.Radiobutton(window, text="Waluty", variable=mode, value="currency")
radio_currency.pack()


window.mainloop()