
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\René Junior\Documents\Cadastro farmacia\build\assets\frame5")


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
    217.0,
    101.0,
    1127.0,
    705.0,
    fill="#16453F",
    outline="")

canvas.create_text(
    553.0,
    167.0,
    anchor="nw",
    text="Insira os dados da sua empressa",
    fill="#A6F6AF",
    font=("Inter SemiBold", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    background="#16453F",
)
button_1.place(
    x=603.0,
    y=677.0,
    width=150.0,
    height=19.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    665.0,
    564.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 25),
)
entry_1.place(
    x=256.0,
    y=540.0,
    width=818.0,
    height=47.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    665.0,
    409.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 25),
)
entry_2.place(
    x=256.0,
    y=385.0,
    width=818.0,
    height=47.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    665.0,
    485.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 25),
)
entry_3.place(
    x=256.0,
    y=460.0,
    width=818.0,
    height=48.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    456.0,
    334.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 25),
)
entry_4.place(
    x=256.0,
    y=309.0,
    width=400.0,
    height=48.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    876.0,
    334.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 25),
)
entry_5.place(
    x=678.0,
    y=309.0,
    width=396.0,
    height=48.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    665.0,
    255.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#EEF4EC",
    fg="#000716",
    highlightthickness=0,
    font=("Arial", 25),
)
entry_6.place(
    x=256.0,
    y=231.0,
    width=818.0,
    height=47.0
)

canvas.create_text(
    256.0,
    202.0,
    anchor="nw",
    text="Razão Social",
    fill="#EEF4EC",
    font=("Inter SemiBold", 25 * -1)
)

canvas.create_text(
    256.0,
    512.0,
    anchor="nw",
    text="Confirmar senha ",
    fill="#EEF4EC",
    font=("Inter SemiBold", 25 * -1)
)

canvas.create_text(
    256.0,
    359.0,
    anchor="nw",
    text="Logradouro",
    fill="#EEF4EC",
    font=("Inter SemiBold", 25 * -1)
)

canvas.create_text(
    256.0,
    433.0,
    anchor="nw",
    text="Senha",
    fill="#EEF4EC",
    font=("Inter SemiBold", 25 * -1)
)

canvas.create_text(
    256.0,
    280.0,
    anchor="nw",
    text="CNPJ",
    fill="#EEF4EC",
    font=("Inter SemiBold", 25 * -1)
)

canvas.create_text(
    678.0,
    280.0,
    anchor="nw",
    text="CEP",
    fill="#EEF4EC",
    font=("Inter SemiBold", 25 * -1)
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
    x=571.0,
    y=610.0,
    width=213.0,
    height=63.0
)

canvas.create_text(
    531.0,
    122.0,
    anchor="nw",
    text="Crie sua conta",
    fill="#F9F9F9",
    font=("Inter Bold", 40 * -1)
)
window.resizable(False, False)
window.mainloop()
