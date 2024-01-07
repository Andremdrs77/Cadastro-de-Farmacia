
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\Imagens")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class TelaLogin():
    def __init__(self):
        self.window = Tk()

        self.window.geometry("1356x826")
        self.window.configure(bg = "#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 826,
            width = 1356,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            404.0,
            137.0,
            952.0,
            689.0,
            fill="#16453F",
            outline="")

        self.canvas.create_text(
            624.0,
            187.0,
            anchor="nw",
            text="Login",
            fill="#EEF4EC",
            font=("Inter Bold", 40 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command= self.login,
            relief="flat"
        )
        self.button_1.place(
            x=578.0,
            y=509.0,
            width=194.0,
            height=80.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            678.0,
            320.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 25)
        )
        self.entry_1.place(
            x=451.0,
            y=280.0,
            width=454.0,
            height=78.0
        )

        self.canvas.create_text(
            451.0,
            251.0,
            anchor="nw",
            text="CNPJ",
            fill="#EEF4EC",
            font=("Inter Bold", 24 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            678.0,
            431.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 25),
        )
        self.entry_2.place(
            x=451.0,
            y=391.0,
            width=454.0,
            height=78.0
        )

        self.canvas.create_text(
            450.0,
            362.0,
            anchor="nw",
            text="Palavra-passe",
            fill="#EEF4EC",
            font=("Inter Bold", 24 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat",
            background="#16453F",
        )
        self.button_2.place(
            x=583.0,
            y=620.0,
            width=194.0,
            height=29.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def login(self):
        cnpj = self.entry_1.get()
        senha = self.entry_2.get()
        banco = crud.banco
        cursor = crud.cursor
        cursor.execute(f"SELECT emp_senha FROM empresa WHERE emp_cnpj = {cnpj}")
        senha_bd = cursor.fetchall()
        print(senha_bd[0])
        banco.close()
        

tela = TelaLogin()