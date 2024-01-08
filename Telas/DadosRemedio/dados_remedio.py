
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

class TelaDadosRemedio:
    def __init__(self):
        
        self.window = Tk()

        self.window.geometry("1356x826")
        self.window.configure(bg = "#E4E6E5")


        self.canvas = Canvas(
            self.window,
            bg = "#E4E6E5",
            height = 826,
            width = 1356,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            117.0,
            85.0,
            1253.0,
            168.0,
            fill="#16453F",
            outline="")

        self.canvas.create_rectangle(
            117.0,
            237.0,
            1253.0,
            279.0,
            fill="#C9CDCA",
            outline="")

        self.canvas.create_rectangle(
            117.0,
            413.0,
            699.0,
            455.0,
            fill="#C9CDCA",
            outline="")

        self.canvas.create_rectangle(
            117.0,
            295.0,
            1253.0,
            333.0,
            fill="#C9CDCA",
            outline="")

        self.canvas.create_rectangle(
            722.0,
            349.0,
            1253.0,
            393.0,
            fill="#C9CDCA",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=522.0,
            y=534.0,
            width=312.0,
            height=59.0
        )

        self.canvas.create_text(
            130.0,
            299.0,
            anchor="nw",
            text="Empresa:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            125.0,
            245.0,
            anchor="nw",
            text="Nome: ",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            125.0,
            421.0,
            anchor="nw",
            text="Preço:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            118.0,
            189.0,
            anchor="nw",
            text="Dados da Clínica",
            fill="#000000",
            font=("Inter", 32 * -1)
        )

        self.canvas.create_text(
            410.0,
            87.0,
            anchor="nw",
            text="Dados do remédio",
            fill="#FFFFFF",
            font=("Inter Bold", 64 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_2 clicked"),
            relief="flat",
            background="#E4E6E5"
        )
        self.button_2.place(
            x=107.0,
            y=30.0,
            width=169.0,
            height=37.0
        )

        self.canvas.create_text(
            733.0,
            358.0,
            anchor="nw",
            text="Tipo:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_rectangle(
            722.0,
            413.0,
            1253.0,
            455.0,
            fill="#C9CDCA",
            outline="")

        self.canvas.create_text(
            731.0,
            421.0,
            anchor="nw",
            text="Marca:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_rectangle(
            117.0,
            353.0,
            193.0,
            391.0,
            fill="#C9CDCA",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            408.5,
            372.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#C9CDCA",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15)
        )
        self.entry_1.place(
            x=199.0,
            y=353.0,
            width=419.0,
            height=36.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=624.0,
            y=353.0,
            width=75.0,
            height=38.0
        )

        self.canvas.create_text(
            126.0,
            359.0,
            anchor="nw",
            text="Lote:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )
        self.window.resizable(False, False)