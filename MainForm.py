import tkinter as tk
import tkinter.messagebox as messagebox
import AddCart

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("DevTool")
        self.master.iconbitmap("icons/toolbox.ico")
        self.master.geometry("800x600")
        self.master.configure(bg="#363636")
        title = tk.Label(
            self.master
            , text="Elektrum DevTool"
            , font=("Calibri", 24)
            , padx=20
            , pady=20
            ,bg="#363636"
            ,fg="#ffffff")
        title.pack(side="top")
        button = tk.Button(
            self.master
            , text="Add Card"
            , width=20
            , height=3
            ,command= AddCart.AddCardForm)
        button.pack() 


