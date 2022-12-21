from tkinter import *
root = Tk()
root.title("GCity Railways")
root.geometry("800x800")
exit_button = Button(root, text="Exit", command=root.destroy).place(x=0, y=0)
root.mainloop()