import customtkinter as CTk
import CTkToolTip as CTkTT
from PIL import Image

class spells_frame(CTk.Frame):
    def __init__(self):
        super().__init__()

class inventory_frame(CTk.Frame):
    def __init__(self):
        super().__init__()

class money_frame(CTk.Frame):
    def __init__(self):
        super().__init__()

class other_abilities(CTk.Frame):
    def __init__(self):
        super().__init__()

class class_abilities(CTk.Frame):
    def __init__(self):
        super().__init__()

class feats_frame(CTk.Frame):
    def __init__(self):
        super().__init__()

class stat_frame(CTk.Frame):
    def __init__(self):
        super().__init__()        

class class_frame(CTk.Frame):
    def __init__(self):
        super().__init__()

class Main(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("D&D 2024 Character Sheet")
        self.geometry("100x100")

sheet = Main()
sheet.mainloop()