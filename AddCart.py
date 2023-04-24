import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.font as tkFont
import XMLExport as xmlE


class AddCardForm():
    def __init__(self):
        my_font = tkFont.Font(family="Calibri", size=14, weight="normal")
        h1Font = tkFont.Font(family="Calibri", size=24, weight="bold")
        self.dialog_window = tk.Toplevel()
        self.dialog_window.grab_set()
        self.dialog_window.geometry("400x700")
        self.dialog_window.configure(bg="#363636")
        self.dialog_window.title("Dialog Window")     
        #title
        self.message_label = tk.Label(
            self.dialog_window
            , text="Create Custom Card."
            ,font=h1Font
            ,bg="#363636"
            ,fg="#ffffff")
        self.message_label.pack()

        self.AdrenCostLabel = tk.Label(
            self.dialog_window
            , text="Declare Adrenaline Cost"
            ,font=my_font
            ,bg="#363636"
            ,fg="#ffffff")
        self.AdrenCostLabel.pack()

        # tworzenie elementu Entry z początkową wartością
        self.AdrenCostText = tk.Text(
            self.dialog_window
            , width=30
            ,height=2)
        self.AdrenCostText.pack()
        #name
        self.NameLabel = tk.Label(
            self.dialog_window
            , text="Declare Name"
            ,font=my_font
            ,bg="#363636"
            ,fg="#ffffff")
        self.NameLabel.pack()

        # tworzenie elementu Entry z początkową wartością
        self.NameLabeltext = tk.Text(
            self.dialog_window
            , width=30
            ,height=2)
        self.NameLabeltext.pack()
        
        #description
        self.DescriptionLabel = tk.Label(
            self.dialog_window
            , text="Declare Description"
            ,font=my_font
            ,bg="#363636"
            ,fg="#ffffff")
        self.DescriptionLabel.pack()

        # tworzenie elementu Entry z początkową wartością
        self.Descriptiontext = tk.Text(
            self.dialog_window
            , width=30
            ,height=25)
        self.Descriptiontext.pack()

        #submit
        self.ok_button = tk.Button(
            self.dialog_window
            , text="Wyślij"
            , command=self.submit
            ,padx=10
            ,pady=10)
        self.ok_button.pack(side="bottom")
    def submit(self):
        try:
            num = int(self.AdrenCostText.get("1.0",tk.END))
            xmlE.Export(
                num
                ,self.Descriptiontext.get("1.0",tk.END)
                ,self.NameLabeltext.get("1.0",tk.END))
        except ValueError:
    # Zgłoś błąd, że przekazany tekst nie jest liczbą
            messagebox.showerror(
                "Podany text nie jest liczbą"
                ,"Podany text nie jest liczbą")
            return

        self.dialog_window.destroy()
  