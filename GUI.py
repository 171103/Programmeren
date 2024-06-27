import tkinter as tk

def begroet():
    naam = naam_entry.get()
    begroeting_label.config(text=f"Welkom, {naam}!")

# Maak een hoofdvenster
root = tk.Tk()
root.title("Welkom door ChatGPT")

# Stel het vensterformaat in
root.geometry("400x200")

# Maak een welkomstlabel
welkomst_label = tk.Label(root, text="Voer je naam in:", font=("Arial", 14), bg="lightblue", fg="black")
welkomst_label.pack(pady=10)

# Maak een invoerveld
naam_entry = tk.Entry(root, font=("Arial", 14), bg="white", fg="blue")
naam_entry.pack(pady=10)

# Maak een label om de begroeting te tonen
begroeting_label = tk.Label(root, text="", font=("Arial", 14), bg="lightgreen", fg="black")
begroeting_label.pack(pady=10)

# Maak een knop om de begroeting te activeren
begroet_button = tk.Button(root, text="Begroet", command=begroet, font=("Arial", 14), bg="blue", fg="white")
begroet_button.pack(pady=10)

# Start de hoofdloop van de GUI
root.mainloop()
