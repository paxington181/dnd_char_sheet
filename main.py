import customtkinter as CTk
import CTkToolTip as CTkTT
from PIL import Image

class Main(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("D&D 2024 Character Sheet")
        self.geometry("100x100")

sheet = Main()
sheet.mainloop()