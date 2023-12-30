
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame4")


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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    124.99999838826625,
    47.99999837707202,
    image=image_image_1
)

canvas.create_rectangle(
    117.0,
    85.0,
    1253.0,
    168.0,
    fill="#16453F",
    outline="")

canvas.create_rectangle(
    117.0,
    237.0,
    1253.0,
    279.0,
    fill="#C9CDCA",
    outline="")

canvas.create_rectangle(
    118.0,
    471.0,
    700.0,
    513.0,
    fill="#C9CDCA",
    outline="")

canvas.create_rectangle(
    118.0,
    353.0,
    700.0,
    391.0,
    fill="#C9CDCA",
    outline="")

canvas.create_rectangle(
    723.0,
    407.0,
    1254.0,
    451.0,
    fill="#C9CDCA",
    outline="")

canvas.create_rectangle(
    119.0,
    407.0,
    700.0,
    450.0,
    fill="#C9CDCA",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=529.0,
    y=655.0,
    width=312.0,
    height=59.0
)

canvas.create_text(
    131.0,
    357.0,
    anchor="nw",
    text="Senha: ********",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    132.0,
    245.0,
    anchor="nw",
    text="Nome: ",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    117.0,
    294.0,
    1253.0,
    336.0,
    fill="#C9CDCA",
    outline="")

canvas.create_text(
    131.0,
    304.0,
    anchor="nw",
    text="Empresa:",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    126.0,
    479.0,
    anchor="nw",
    text="CEP",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    118.0,
    189.0,
    anchor="nw",
    text="Dados do vendedor",
    fill="#000000",
    font=("Inter", 32 * -1)
)

canvas.create_text(
    377.0,
    87.0,
    anchor="nw",
    text="Dados do vendedor",
    fill="#FFFFFF",
    font=("Inter Bold", 64 * -1)
)

canvas.create_text(
    150.0,
    34.0,
    anchor="nw",
    text="Voltar",
    fill="#000000",
    font=("Inter SemiBold", 26 * -1)
)

canvas.create_text(
    734.0,
    416.0,
    anchor="nw",
    text="Telefone",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    613.0,
    416.0,
    anchor="nw",
    text="Editar",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    723.0,
    471.0,
    1254.0,
    513.0,
    fill="#C9CDCA",
    outline="")

canvas.create_text(
    732.0,
    479.0,
    anchor="nw",
    text="Data de Nascimento",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    613.0,
    360.0,
    anchor="nw",
    text="Editar",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    723.0,
    353.0,
    1254.0,
    391.0,
    fill="#C9CDCA",
    outline="")

canvas.create_text(
    736.0,
    357.0,
    anchor="nw",
    text="CPF",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    1175.0,
    360.0,
    anchor="nw",
    text="Editar",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    1175.0,
    301.0,
    anchor="nw",
    text="Editar",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    118.0,
    536.0,
    700.0,
    574.0,
    fill="#C9CDCA",
    outline="")

canvas.create_text(
    131.0,
    540.0,
    anchor="nw",
    text="Endereço",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    579.0,
    540.0,
    anchor="nw",
    text="Adicionar",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    579.0,
    479.0,
    anchor="nw",
    text="Adicionar",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    1136.0,
    416.0,
    anchor="nw",
    text="Adicionar",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    1136.0,
    479.0,
    anchor="nw",
    text="Adicionar",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    723.0,
    531.0,
    1254.0,
    573.0,
    fill="#C9CDCA",
    outline="")

canvas.create_text(
    732.0,
    539.0,
    anchor="nw",
    text="Complemento",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    1136.0,
    540.0,
    anchor="nw",
    text="Adicionar",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    129.0,
    416.0,
    anchor="nw",
    text="E-mail",
    fill="#000000",
    font=("Inter", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
