from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox


window = Tk()
window.geometry('1000x800')
window.title("Music Player")
#window.configure(bg="black")
img = Image.open("back.jpg")
bg = ImageTk.PhotoImage(img)

label = Label(window, image=bg)
label.place(x=0,y=0)


mixer.init()


def help_me():
    tkinter.messagebox.showinfo("Help", "How can I help you?")


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


menubar = Menu(window)
submenu = Menu(menubar, tearoff=0)
window.config(menu=menubar)

menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=window.destroy)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About Us", menu=submenu)
submenu.add_command(label="Help", command=help_me)


def play():
    try:
        paused
    except:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar["text"] = "Music is playing"
        except:
            tkinter.messagebox.showerror("File Error", "File not found")
    else:
        mixer.music.unpause()
        statusbar["text"] = "Music is resumed"


def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar["text"] = "Music is paused"


def set_volume(value):
    volume = int(value)/100
    mixer.music.set_volume(volume)


def stop():
    mixer.music.stop()
    statusbar["text"]= "Music is stopped"


def rewind_music():
    play()
    statusbar["text"] = "Music is rewinded"


frame = Frame(window)
frame.pack(padx=10, pady=10)


photo = PhotoImage(file="play.png")
play_button = Button(frame, image=photo, command=play, height=200, width=200)
play_button.grid(row=0, column=0, padx=10)

pause = PhotoImage(file="pause.png")
pause_button = Button(frame, image=pause, command=pause_music, height=200, width=200)
pause_button.grid(row=0, column=1, padx=10)

stop_photo = PhotoImage(file="stop.png")
stop_button = Button(frame, image=stop_photo, command=stop, height=200, width=200)
stop_button.grid(row=0, column=2, padx=10)

bottom = Frame(window)
bottom.pack()

rewind = PhotoImage(file="rewind.png")
rewind_button = Button(bottom, image=rewind, command=rewind_music)
rewind_button.grid(row=0, column=0)

scale = Scale(bottom, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(70)
scale.grid(row=0, column=1)

statusbar = Label(window, text="Enjoying your music",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

window.mainloop()