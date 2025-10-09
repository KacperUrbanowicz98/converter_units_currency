import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

list_options = ["Długość", "Waga", "Waluta"]
options_label = tk.Label(window, text="Kategoria:", font=("Arial", 12, "bold"))
options_label.pack(pady=10)
options_combo = ttk.Combobox(window, values=list_options)
options_combo.current(0)
options_combo.pack()

list_from = ["mm", "cm", "m", "inch", "feet"]
from_label = tk.Label(window, text="Z:", font=("Arial", 12, "bold"))
from_label.pack(pady=10)
from_combo = ttk.Combobox(window, values=list_from)
from_combo.current(1)
from_combo.pack()

from_entry = tk.Entry(window, width=20)
from_entry.pack(pady=5)

list_to = ["mm", "cm", "m", "inch", "feet"]
to_label = tk.Label(window, text="Do:", font=("Arial", 12, "bold"))
to_label.pack(pady=10)
to_combo = ttk.Combobox(window, values=list_to)
to_combo.current(3)
to_combo.pack()

to_entry = tk.Entry(window, state="readonly", width=20)
to_entry.pack(pady=5)

length_to_cm = {
    "mm": 0.1,
    "cm": 1,
    "m": 100,
    "inch": 2.54,
    "feet": 30.48
}


def convert():
    number = from_entry.get()
    if not number:
        messagebox.showwarning("Błąd", "Podaj wartość do konwersji!")
        return
    try:
        number_float = float(number)

        units_from = from_combo.get()
        units_to = to_combo.get()

        value_in_cm = number_float * length_to_cm[units_from]
        result = value_in_cm / length_to_cm[units_to]

        result_rounded = round(result, 2)

        to_entry.config(state="normal")
        to_entry.delete(0, tk.END)
        to_entry.insert(0, str(result_rounded))
        to_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawną liczbę!")



button_convert = tk.Button(window, text="Konwertuj", command=convert)
button_convert.pack()

window.mainloop()