import tkinter as tk
from tkinter import messagebox
import datetime

def bereken_leeftijd():
    try:
        geboortejaar = int(geboortejaar_entry.get())
        huidig_jaar = datetime.datetime.now().year
        leeftijd = huidig_jaar - geboortejaar
        resultaat_label.config(text=f"Je bent dit jaar {leeftijd} jaar oud.")
    except ValueError:
        messagebox.showerror("Ongeldig invoer", "Voer een geldig jaartal in.")
        geboortejaar_entry.delete(0, tk.END)

def clear_input():
    geboortejaar_entry.delete(0, tk.END)
    resultaat_label.config(text="")

# Maak een hoofdvenster
root = tk.Tk()
root.title("Leeftijd Calculator")

# Geboortejaar label en invoer
geboortejaar_label = tk.Label(root, text="Vul je geboortejaar in:", font=("Arial", 14))
geboortejaar_label.grid(row=0, column=0, padx=10, pady=10)

geboortejaar_entry = tk.Entry(root, font=("Arial", 14))
geboortejaar_entry.grid(row=0, column=1, padx=10, pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=bereken_leeftijd, font=("Arial", 14), bg="blue", fg="white")
submit_button.grid(row=1, column=0, padx=10, pady=10)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_input, font=("Arial", 14), bg="red", fg="white")
clear_button.grid(row=1, column=1, padx=10, pady=10)

# Resultaat label
resultaat_label = tk.Label(root, text="", font=("Arial", 14))
resultaat_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start de hoofdloop van de GUI
root.mainloop()
