
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


window = Tk()

window.geometry("1356x826")
window.configure(bg = "#E4E6E5")


canvas = Canvas(
    window,
    bg = "#E4E6E5",
    height = 826,
    width = 1356,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    117.0,
    85.0,
    1253.0,
    168.0,
    fill="#16453F",
    outline="")

canvas.create_rectangle(
    117.0,
    238.0,
    1253.0,
    280.0,
    fill="#C9CDCA",
    outline="")

canvas.create_rectangle(
    117.0,
    426.0,
    699.0,
    468.0,
    fill="#C9CDCA",
    outline="")

canvas.create_rectangle(
    117.0,
    302.0,
    1253.0,
    340.0,
    fill="#C9CDCA",
    outline="")

canvas.create_rectangle(
    722.0,
    362.0,
    1253.0,
    406.0,
    fill="#C9CDCA",
    outline="")

canvas.create_rectangle(
    118.0,
    362.0,
    699.0,
    405.0,
    fill="#C9CDCA",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
)
button_1.place(
    x=522.0,
    y=549.0,
    width=312.0,
    height=59.0
)

canvas.create_text(
    125.0,
    305.0,
    anchor="nw",
    text="Senha: ********",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    131.0,
    246.0,
    anchor="nw",
    text="Nome: ",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    131.0,
    430.0,
    anchor="nw",
    text="Registro de Vendedores:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    118.0,
    189.0,
    anchor="nw",
    text="Dados da Clínica",
    fill="#000000",
    font=("Inter", 32 * -1)
)

canvas.create_text(
    394.0,
    89.0,
    anchor="nw",
    text="Dados da empresa",
    fill="#FFFFFF",
    font=("Inter Bold", 64 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    background="#E4E6E5",
)
button_2.place(
    x=107.0,
    y=30.0,
    width=169.0,
    height=37.0
)

canvas.create_text(
    733.0,
    370.0,
    anchor="nw",
    text="CNPJ:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    722.0,
    426.0,
    1253.0,
    468.0,
    fill="#C9CDCA",
    outline="")

canvas.create_text(
    733.0,
    433.0,
    anchor="nw",
    text="Registro de Clientes:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    131.0,
    370.0,
    anchor="nw",
    text="E-mail:",
    fill="#000000",
    font=("Inter", 24 * -1)
)
window.resizable(False, False)
window.mainloop()