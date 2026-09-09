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

        self.char_class = ["barbarian"]
        self.char_subclass = None
        self.species = "human"
        self.size = "medium"
        self.background = "acolyte"
        self.level = 1
        self.experience = 0
        self.class_level = [1]
        self.max_hp = 13
        self.current_hp = 13
        self.temp_hp = 0
        self.hit_dice = ["1d12"]
        self.proficiency_bonus = 2
        self.save_proficencies = []
        self.stats = [15, 14, 13, 12, 10, 8]
        self.skills = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.feats = ["magic initiate"]
        self.heroic_insp = True
        self.prepared_spells = []
        self.equipment = []

sheet = Main()
sheet.mainloop()