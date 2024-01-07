
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

class TelaDadosCliente:
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

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_1 clicked"),
            relief="flat",
            background="#E4E6E5"
        )
        self.button_1.place(
            x=107.0,
            y=30.0,
            width=169.0,
            height=37.0
        )

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
            699.0,
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

        self.canvas.create_rectangle(
            118.0,
            349.0,
            699.0,
            392.0,
            fill="#C9CDCA",
            outline="")

        self.canvas.create_rectangle(
            722.0,
            413.0,
            1253.0,
            455.0,
            fill="#C9CDCA",
            outline="")

        self.canvas.create_rectangle(
            722.0,
            295.0,
            798.0,
            333.0,
            fill="#C9CDCA",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            1028.5,
            314.0,
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
            x=804.0,
            y=295.0,
            width=449.0,
            height=36.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_2 clicked"),
            relief="flat",
        )
        self.button_2.place(
            x=1268.0,
            y=295.0,
            width=75.0,
            height=38.0
        )

        self.canvas.create_rectangle(
            117.0,
            478.0,
            1253.0,
            515.0,
            fill="#C9CDCA",
            outline="")

        self.canvas.create_text(
            733.0,
            358.0,
            anchor="nw",
            text="Telefone:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            414.0,
            87.0,
            anchor="nw",
            text="Dados do cliente",
            fill="#FFFFFF",
            font=("Inter Bold", 64 * -1)
        )

        self.canvas.create_text(
            132.0,
            245.0,
            anchor="nw",
            text="”Nome:“",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            125.0,
            421.0,
            anchor="nw",
            text="CEP:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            118.0,
            189.0,
            anchor="nw",
            text="Dados do cliente",
            fill="#000000",
            font=("Inter", 32 * -1)
        )

        self.canvas.create_text(
            130.0,
            299.0,
            anchor="nw",
            text="Senha:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            731.0,
            421.0,
            anchor="nw",
            text="Data de Nascimento:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            735.0,
            299.0,
            anchor="nw",
            text="CPF:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            130.0,
            482.0,
            anchor="nw",
            text="Endereço:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            128.0,
            358.0,
            anchor="nw",
            text="E-mail:",
            fill="#000000",
            font=("Inter", 24 * -1)
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
            x=529.0,
            y=596.0,
            width=312.0,
            height=59.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()
