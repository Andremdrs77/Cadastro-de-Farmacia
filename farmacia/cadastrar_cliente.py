
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame7")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1356x826")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 826,
    width = 1356,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    973.0,
    -1.0,
    976.000000035664,
    826.0000289607269,
    fill="#16453F",
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
    x=1024.0,
    y=333.0,
    width=284.0,
    height=160.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1024.0,
    y=46.0,
    width=284.0,
    height=160.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=1024.0,
    y=620.0,
    width=284.0,
    height=160.0
)

canvas.create_rectangle(
    37.0,
    46.0,
    947.0,
    780.0,
    fill="#16453F",
    outline="")

canvas.create_text(
    367.0,
    137.0,
    anchor="nw",
    text="Insira os dados do cliente",
    fill="#A6F6AF",
    font=("Inter SemiBold", 14 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=385.0,
    y=673.0,
    width=213.0,
    height=63.0
)

canvas.create_text(
    307.0,
    75.0,
    anchor="nw",
    text="Cadastrar cliente",
    fill="#F9F9F9",
    font=("Inter Bold", 40 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    490.0,
    192.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=104.0,
    y=168.0,
    width=772.0,
    height=47.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    281.0,
    261.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=104.0,
    y=236.0,
    width=354.0,
    height=48.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    283.0,
    404.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=106.0,
    y=379.0,
    width=354.0,
    height=48.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    699.0,
    404.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=522.0,
    y=379.0,
    width=354.0,
    height=48.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    703.0,
    261.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=528.0,
    y=236.0,
    width=350.0,
    height=48.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    490.0,
    473.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=104.0,
    y=449.0,
    width=772.0,
    height=47.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    492.0,
    542.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=106.0,
    y=518.0,
    width=772.0,
    height=47.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    492.0,
    611.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=106.0,
    y=587.0,
    width=772.0,
    height=47.0
)

canvas.create_text(
    100.0,
    591.0,
    anchor="nw",
    text="Confirmar senha ",
    fill="#585858",
    font=("Inter SemiBold", 32 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    492.0,
    332.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=106.0,
    y=308.0,
    width=772.0,
    height=47.0
)

canvas.create_text(
    100.0,
    316.0,
    anchor="nw",
    text="Email",
    fill="#585858",
    font=("Inter SemiBold", 30 * -1)
)

canvas.create_text(
    100.0,
    524.0,
    anchor="nw",
    text="Senha",
    fill="#585858",
    font=("Inter SemiBold", 30 * -1)
)

canvas.create_text(
    100.0,
    243.0,
    anchor="nw",
    text="CPF",
    fill="#585858",
    font=("Inter SemiBold", 30 * -1)
)

canvas.create_text(
    515.0,
    386.0,
    anchor="nw",
    text="Data de nascimento",
    fill="#585858",
    font=("Inter SemiBold", 30 * -1)
)

canvas.create_text(
    100.0,
    386.0,
    anchor="nw",
    text="Telefone",
    fill="#585858",
    font=("Inter SemiBold", 30 * -1)
)

canvas.create_text(
    100.0,
    456.0,
    anchor="nw",
    text="Endereço",
    fill="#585858",
    font=("Inter SemiBold", 30 * -1)
)

canvas.create_text(
    528.0,
    243.0,
    anchor="nw",
    text="CEP",
    fill="#585858",
    font=("Inter SemiBold", 30 * -1)
)

canvas.create_text(
    100.0,
    174.0,
    anchor="nw",
    text="Nome",
    fill="#585858",
    font=("Inter SemiBold", 30 * -1)
)
window.resizable(False, False)
window.mainloop()
