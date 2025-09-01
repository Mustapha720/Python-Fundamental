from tkinter import *

def click():
    print('Hello')

window = Tk()
window.geometry("420x420")
window.title("Basic GUI")
icon = PhotoImage(file = 'OIP.png')
window.iconphoto(True, icon)
window.config(background = "red")
label = Label(window, text = 'Hello World!', font=('aerial', 20, 'bold'), fg='green', bg='cyan')
# label.pack()
label.place(x = 0, y = 1)
button = Button(window, text='Click me!!!')
button.config(command = click)
button.config(font=('Ink Free', 20, 'bold'), bg = '#ff6200', fg = '#fffb1f')
button.config(activebackground = "#FFF000")
button.config(activeforeground = "#fffb1f")
image = PhotoImage(file = "svgexport-28.png")
button.config(image=image)
button.place(x = 0, y = 42)
window.mainloop()