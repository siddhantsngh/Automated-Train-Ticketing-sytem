from tkinter import *
root = Tk()
root.title("GCity Railways")
root.geometry("400x300")
header = Label(root, text="GCity Railways").pack()
exit_button = Button(root, text="Exit", command=root.destroy).place(x=180, y=130)
root.mainloop()