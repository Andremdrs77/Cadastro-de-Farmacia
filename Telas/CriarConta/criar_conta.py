
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
class TelaCriarConta:
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
            217.0,
            101.0,
            1127.0,
            705.0,
            fill="#16453F",
            outline="")

        self.canvas.create_text(
            553.0,
            167.0,
            anchor="nw",
            text="Insira os dados da sua empresa",
            fill="#A6F6AF",
            font=("Inter SemiBold", 14 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
            background="#16453F",
        )
        self.button_1.place(
            x=603.0,
            y=677.0,
            width=150.0,
            height=19.0
        )

        # EMAIL

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            665.0,
            409.5,
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
            x=256.0,
            y=385.0,
            width=818.0,
            height=47.0
        )

        # SENHA

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            665.0,
            485.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 25),
        )
        self.entry_3.place(
            x=256.0,
            y=460.0,
            width=818.0,
            height=48.0
        )

        # CNPJ

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            456.0,
            334.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 25),
        )
        self.entry_4.place(
            x=256.0,
            y=309.0,
            width=400.0,
            height=48.0
        )

        # CEP

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            876.0,
            334.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 25),
        )
        self.entry_5.place(
            x=678.0,
            y=309.0,
            width=396.0,
            height=48.0
        )

        # RAZÃO SOCIAL

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            665.0,
            255.5,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 25),
        )
        self.entry_6.place(
            x=256.0,
            y=231.0,
            width=818.0,
            height=47.0
        )

        self.canvas.create_text(
            256.0,
            202.0,
            anchor="nw",
            text="Razão Social",
            fill="#EEF4EC",
            font=("Inter SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            256.0,
            359.0,
            anchor="nw",
            text="E-mail",
            fill="#EEF4EC",
            font=("Inter SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            256.0,
            433.0,
            anchor="nw",
            text="Senha",
            fill="#EEF4EC",
            font=("Inter SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            256.0,
            280.0,
            anchor="nw",
            text="CNPJ",
            fill="#EEF4EC",
            font=("Inter SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            678.0,
            280.0,
            anchor="nw",
            text="CEP",
            fill="#EEF4EC",
            font=("Inter SemiBold", 25 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=571.0,
            y=610.0,
            width=213.0,
            height=63.0
        )

        self.canvas.create_text(
            531.0,
            122.0,
            anchor="nw",
            text="Crie sua conta",
            fill="#F9F9F9",
            font=("Inter Bold", 40 * -1)
        )
        self.window.resizable(False, False)