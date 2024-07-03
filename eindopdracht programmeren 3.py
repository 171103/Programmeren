import tkinter as tk
from tkinter import ttk

class RekentoolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Rekentool Applicatie")
        self.geometry("600x500")
        
        self.create_menu()
        self.show_frame(StartPage)
    
    def create_menu(self):
        menubar = tk.Menu(self)
        
        # Menu item 'Rekentools'
        rekentool_menu = tk.Menu(menubar, tearoff=0)
        rekentool_menu.add_command(label="BTW Berekenen", command=lambda: self.show_frame(BtwPage))
        rekentool_menu.add_command(label="Reistijd Berekenen", command=lambda: self.show_frame(ReistijdPage))
        rekentool_menu.add_command(label="Vierkant Berekenen", command=lambda: self.show_frame(VierkantPage))
        rekentool_menu.add_command(label="Cirkel Berekenen", command=lambda: self.show_frame(CirkelPage))
        menubar.add_cascade(label="Rekentools", menu=rekentool_menu)
        
        self.config(menu=menubar)
    
    def show_frame(self, page):
        frame = page(self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="Welkom bij de Rekentool Applicatie bij Tim Bos", font=("Arial", 16))
        label.pack(pady=20)

class BtwPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="BTW Berekening", font=("Arial", 16))
        label.pack(pady=20)
        
        self.amount_label = tk.Label(self, text="Bedrag excl. BTW:")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=5)
        
        self.btw_label = tk.Label(self, text="BTW percentage:")
        self.btw_label.pack(pady=5)
        self.btw_entry = tk.Entry(self)
        self.btw_entry.pack(pady=5)
        
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=20)
        
        self.calc_button = tk.Button(self, text="Bereken BTW", command=self.calculate_btw)
        self.calc_button.pack(pady=10)
    
    def calculate_btw(self):
        try:
            amount = float(self.amount_entry.get())
            btw_percentage = float(self.btw_entry.get())
            btw_amount = amount * (btw_percentage / 100)
            total_amount = amount + btw_amount
            self.result_label.config(text=f"Bedrag incl. BTW: {total_amount:.2f} EUR")
        except ValueError:
            self.result_label.config(text="Voer geldige waarden in.")

class ReistijdPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="Reistijd Berekening", font=("Arial", 16))
        label.pack(pady=20)
        
        self.distance_label = tk.Label(self, text="Afstand (km):")
        self.distance_label.pack(pady=5)
        self.distance_entry = tk.Entry(self)
        self.distance_entry.pack(pady=5)
        
        self.speed_label = tk.Label(self, text="Snelheid (km/h):")
        self.speed_label.pack(pady=5)
        self.speed_entry = tk.Entry(self)
        self.speed_entry.pack(pady=5)
        
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=20)
        
        self.calc_button = tk.Button(self, text="Bereken Reistijd", command=self.calculate_time)
        self.calc_button.pack(pady=10)
    
    def calculate_time(self):
        try:
            distance = float(self.distance_entry.get())
            speed = float(self.speed_entry.get())
            time = distance / speed
            self.result_label.config(text=f"Reistijd: {time:.2f} uur")
        except ValueError:
            self.result_label.config(text="Voer geldige waarden in.")

class VierkantPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="Vierkant Berekening", font=("Arial", 16))
        label.pack(pady=20)
        
        self.length_label = tk.Label(self, text="Lengte:")
        self.length_label.pack(pady=5)
        self.length_entry = tk.Entry(self)
        self.length_entry.pack(pady=5)
        
        self.width_label = tk.Label(self, text="Breedte:")
        self.width_label.pack(pady=5)
        self.width_entry = tk.Entry(self)
        self.width_entry.pack(pady=5)
        
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=20)
        
        self.calc_button = tk.Button(self, text="Bereken Omtrek & Oppervlakte", command=self.calculate_vierkant)
        self.calc_button.pack(pady=10)
    
    def calculate_vierkant(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            omtrek = 2 * (length + width)
            oppervlakte = length * width
            self.result_label.config(text=f"Omtrek: {omtrek:.2f} \nOppervlakte: {oppervlakte:.2f}")
        except ValueError:
            self.result_label.config(text="Voer geldige waarden in.")

class CirkelPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="Cirkel Berekening", font=("Arial", 16))
        label.pack(pady=20)
        
        self.diameter_label = tk.Label(self, text="Diameter:")
        self.diameter_label.pack(pady=5)
        self.diameter_entry = tk.Entry(self)
        self.diameter_entry.pack(pady=5)
        
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=20)
        
        self.calc_button = tk.Button(self, text="Bereken Omtrek & Oppervlakte", command=self.calculate_cirkel)
        self.calc_button.pack(pady=10)
    
    def calculate_cirkel(self):
        try:
            diameter = float(self.diameter_entry.get())
            straal = diameter / 2
            omtrek = 2 * 3.141592653589793 * straal
            oppervlakte = 3.141592653589793 * (straal ** 2)
            self.result_label.config(text=f"Omtrek: {omtrek:.2f} \nOppervlakte: {oppervlakte:.2f}")
        except ValueError:
            self.result_label.config(text="Voer geldige waarden in.")

if __name__ == "__main__":
    app = RekentoolApp()
    app.mainloop()
