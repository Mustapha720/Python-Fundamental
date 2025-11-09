from tkinter import *

def click():
    print('Hello')

window = Tk()
window.geometry("420x420")
window.title("Basic GUI")
icon = PhotoImage(file = 'OIP.png')
window.iconphoto(True, icon)
window.config(background = "red")
photo = PhotoImage(file='')
label = Label(window, text = 'Hello World!',
            font=('aerial', 20, 'bold'),
            fg='green',
            bg='black',
            relief= RAISED,
            bd= 10,
            padx= 20,
            pady= 20
            )
# label.pack()
label.place(x = 0, y = 1)
button = Button(window, text='Click me!!!')
button.config(command = click)
button.config(font=('Ink Free', 20, 'bold'), bg = '#ff6200', fg = '#fffb1f')
button.config(activebackground = "#FFF000")
button.config(activeforeground = "#fffb1f")
image = PhotoImage(file = "svgexport-28.png")
button.config(image=image)
button.place(x = 0, y = 92)
window.mainloop()