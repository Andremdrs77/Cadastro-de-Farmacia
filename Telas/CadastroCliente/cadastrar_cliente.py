
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


class TelaCadastrarCliente:
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
            973.0,
            -1.0,
            976.000000035664,
            826.0000289607269,
            fill="#16453F",
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
            x=1024.0,
            y=333.0,
            width=284.0,
            height=160.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=1024.0,
            y=46.0,
            width=284.0,
            height=160.0
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
            x=1024.0,
            y=620.0,
            width=284.0,
            height=160.0
        )

        self.canvas.create_rectangle(
            37.0,
            86.0,
            947.0,
            740.0,
            fill="#16453F",
            outline="")

        self.canvas.create_text(
            414.0,
            142.0,
            anchor="nw",
            text="Insira os dados do cliente",
            fill="#A6F6AF",
            font=("Inter SemiBold", 14 * -1)
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=385.0,
            y=652.0,
            width=213.0,
            height=63.0
        )

        self.canvas.create_text(
            326.0,
            97.0,
            anchor="nw",
            text="Cadastrar cliente",
            fill="#F9F9F9",
            font=("Inter Bold", 40 * -1)
        )

        # NOME

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            492.0,
            190.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15),
        )
        self.entry_1.place(
            x=82.0,
            y=174.0,
            width=820.0,
            height=30.0
        )

        # CPF

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            282.0,
            265.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15),
        )
        self.entry_2.place(
            x=82.0,
            y=247.0,
            width=400.0,
            height=34.0
        )

        # TELEFONE

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            283.0,
            420.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15),
        )
        self.entry_3.place(
            x=83.0,
            y=402.0,
            width=400.0,
            height=34.0
        )

        # DATA NASCIMENTO

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            701.0,
            420.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15),
        )
        self.entry_4.place(
            x=500.0,
            y=402.0,
            width=402.0,
            height=34.0
        )

        # CEP

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            699.0,
            265.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15),
        )
        self.entry_5.place(
            x=499.0,
            y=247.0,
            width=400.0,
            height=36.0
        )

        # ENDEREÇO

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            491.0,
            510.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15),
        )
        self.entry_6.place(
            x=81.0,
            y=492.0,
            width=820.0,
            height=34.0
        )

        # EMAIL

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            491.0,
            342.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15),
        )
        self.entry_7.place(
            x=82.0,
            y=324.0,
            width=818.0,
            height=34.0
        )

        self.canvas.create_text(
            500.0,
            369.0,
            anchor="nw",
            text="Data de nascimento",
            fill="#EEF4EC",
            font=("Inter SemiBold", 30 * -1)
        )

        self.canvas.create_text(
            82.0,
            368.0,
            anchor="nw",
            text="Telefone",
            fill="#EEF4EC",
            font=("Inter SemiBold", 30 * -1)
        )

        # SENHA

        self.entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            491.0,
            589.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#EEF4EC",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 15),
        )
        self.entry_8.place(
            x=81.0,
            y=571.0,
            width=818.0,
            height=34.0
        )


        self.canvas.create_text(
            79.0,
            537.0,
            anchor="nw",
            text="Senha",
            fill="#EEF4EC",
            font=("Inter SemiBold", 30 * -1)
        )

        self.canvas.create_text(
            82.0,
            446.0,
            anchor="nw",
            text="Endereço",
            fill="#EEF4EC",
            font=("Inter SemiBold", 30 * -1)
        )

        self.canvas.create_text(
            83.0,
            134.0,
            anchor="nw",
            text="Nome",
            fill="#EEF4EC",
            font=("Inter SemiBold", 30 * -1)
        )

        self.canvas.create_text(
            81.0,
            210.0,
            anchor="nw",
            text="CPF",
            fill="#EEF4EC",
            font=("Inter SemiBold", 30 * -1)
        )

        self.canvas.create_text(
            82.0,
            283.0,
            anchor="nw",
            text="Email",
            fill="#EEF4EC",
            font=("Inter SemiBold", 30 * -1)
        )

        self.canvas.create_text(
            499.0,
            210.0,
            anchor="nw",
            text="CEP",
            fill="#EEF4EC",
            font=("Inter SemiBold", 30 * -1)
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self.button_5 clicked"),
            relief="flat",
            background="#FFFFFF",
        )
        self.button_5.place(
            x=35.0,
            y=28.0,
            width=169.0,
            height=37.0
        )
        self.window.resizable(False, False)
