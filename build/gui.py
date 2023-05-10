# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Menu
from build.songutils import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\shams\PycharmProjects\MusicPlayer\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("342x491")
window.configure(bg="#FFFFFF")

menubar = Menu()

fileMenu = Menu(menubar)
fileMenu.add_command(label="Open Song",command=lambda :loadsingle())
fileMenu.add_command(label="Open PlayList",command=lambda :loadPlaylist())
menubar.add_cascade(label="File", menu=fileMenu)
menubar.add_command(label="Exit",command=lambda :window.quit())
window.config(menu=menubar)

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=491,
    width=342,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    171.0,
    245.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    171.0,
    323.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: nextSong(),
    relief="flat"
)

button_1.place(
    x=227.0,
    y=311.0,
    width=57.5,
    height=37.5
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pause(),
    relief="flat"
)
button_2.place(
    x=154.0,
    y=225.0,
    width=35.0,
    height=40.0
)

canvas.create_text(
    21.0,
    64.0,
    anchor="nw",
    text="Python Music Player",
    fill="#000000",
    font=("Inter Bold", 30 * -1)
)


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: play(),
    relief="flat"
)
button_3.place(
    x=115.0,
    y=277.0,
    width=112.0,
    height=105.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: prevSong(),
    relief="flat"
)
button_4.place(
    x=58.0,
    y=310.0,
    width=57.5,
    height=37.5
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: stop(),
    relief="flat"
)
button_5.place(
    x=156.0,
    y=400.0,
    width=30.0,
    height=33.0
)
window.resizable(False, False)
window.mainloop()