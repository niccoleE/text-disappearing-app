from tkinter import *
from threading import Thread
from time import sleep

changes = 0
timer = 0


def get_input(event):
    """event on key release"""
    global changes
    global timer

    def change_color(color):
        """change text color before disappearing"""
        text_entry.tag_add("text", f'1.0', END)
        text_entry.tag_config("text", foreground=color)

    def timer_start():
        """start timer"""
        global timer
        if timer < 4.9:
            # # # if decide to make timer_widget visible
            #canvas.itemconfig(timer_widget, text=round(timer))
            timer += 0.1
            sleep(0.1)
            if timer > 4:
                change_color("pink")
            else:
                change_color("black")
            if timer > 4.9:
                text_entry.delete(1.0, END)

    def timer_1():
        """restart timer with each new event)"""
        if changes % 2 != 0:
            timer_start()
            thread = Thread(target=timer_1)
            thread.start()

    def timer_2():
        """restart timer with each new event"""
        if changes != 0 and changes % 2 == 0:
            timer_start()
            thread = Thread(target=timer_2)
            thread.start()

    timer = 0
    changes += 1

    timer_1()
    timer_2()


root = Tk()
root.title('Text Disappearing App')
root.geometry("700x500")
root.config(padx=50, pady=30)

canvas = Canvas(width=700, height=500, highlightthickness=0)
canvas.grid(column=0, row=0, ipadx=30, ipady=30)

label_1 = Label(canvas, font=('arial', 15, 'bold'), text="If you stop typing for more than 5 seconds", fg='#3E065F')
label_2 = Label(canvas, font=('arial', 15, 'bold'), text="all your text will disappear", fg='#3E065F')
label_1.grid(row=0, column=1)
label_2.grid(row=1, column=1, pady=15)

# # # timer widget, if decide to make it visible
#timer_widget = canvas.create_text(570, 18, text="", fill='#054B07', font=('Lucida', 15, 'bold'))

text_entry = Text(canvas, font=('Lucida', 15), width=55, height=14)
text_entry.grid(row=5, column=0, columnspan=3)

text_entry.bind('<KeyRelease>', get_input)

root.mainloop()
