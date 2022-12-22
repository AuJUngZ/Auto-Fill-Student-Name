from tkinter import *
import pyautogui
import keyboard
import time


def start(txt):
    keyboard.wait("enter")
    if (keyboard.is_pressed("enter")):
        # read the text from the text box 1 line automatically
        for line in txt.splitlines():
            if keyboard.is_pressed("esc"):
                break
            x = line.split()
            if len(x) == 2:
                x = x[0] + " " + x[1]
            else:
                x = x[0]
            pyautogui.typewrite(x)
            pyautogui.press("enter")
            # save the text for use next time when the program is run
            with open("text.txt", "w") as f:
                f.write(txt)
            # time.sleep(0.2)


root = Tk()
root.title("กรอกชื่อนักศึกษา")
root.geometry("400x400")
# create a label at center of the window and set the text and font size of the label
label = Label(root, text="กรอกชื่อนักศึกษา", font=("Arial", 20))
label.pack()
# create a text box at center of the window and show scrollbar
textbox = Text(root, height=10, width=30)
textbox.pack()
# leave a line
label = Label(root, text="")
label.pack()
# create a button at center of the window and set the text and font size of the button
button = Button(root, text="Start", font=("Arial", 18))
button.pack()
# when the button is clicked, the function is called
button.config(command=lambda: start(textbox.get("1.0", "end-1c")))
# before clicking the button, show text how to use the program and text color is red
label = Label(root, text="กด Enter ที่ช่องค้นหาชื่อเพื่อเริ่ม กด Esc ค้างไว้เพื่อหยุด", fg="red", font=("Arial", 10))
label2 = Label(root, text="")
label2.pack()
label.pack()

# first time run the program, show the text that was saved
# if first time don't show anything
try:
    with open("text.txt", "r") as f:
        textbox.insert(END, f.read())
except:
    pass
root.mainloop()
# build the exe file
