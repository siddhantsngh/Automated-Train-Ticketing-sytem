from tkinter import *

root = Tk()
root.title('GCity Railways')
root.geometry("1200x700")

# Defining image
bg = PhotoImage(file=r"C:\Users\91998\Downloads\project_11zon (1).png")

# Create a canvas
Canvas1 = Canvas(root, width=1200, height=700)
Canvas1.pack(fill="both", expand=True)

# Set image in canvas
Canvas1.create_image(0,0, image=bg, anchor="nw")

#Functions
def CLEAR():
    e2.delete(0, END)










# Add labels
Canvas1.create_text(600, 50, text="GrandCity Railways", font=("Helvetica", 30), fill="white")
Canvas1.create_text(160, 312, text="Enter SIN : ", font=("Arial", 10), fill="white")
#Canvas1.create_text(600, 50, text="GrandCity Railways", font=("Helvetica", 30), fill="white")

#Making Input boxes
e1 = Entry(root, width=20, borderwidth=5)
e2 = Entry(root,width=30,borderwidth=5)
e3 = Entry(root,width=30,borderwidth=5)

# Making buttons
button1 = Button(root, text="Submit")
button2 = Button(root, text="Track your train")
button3 = Button(root, text="Exit window",padx=10, pady=10,command=root.quit)
button4 = Button(root, text="Destination Reached")
button5 = Button(root, text="Clear",command=CLEAR)

# Adding buttons to the canvas
button1_window = Canvas1.create_window(240, 350, anchor="nw", window=button1)
button2_window = Canvas1.create_window(1000, 500, anchor="nw", window=button2)
button3_window = Canvas1.create_window(600, 650, anchor="nw", window=button3)
button4_window = Canvas1.create_window(210, 500, anchor="nw", window=button4)
button5_window = Canvas1.create_window(250, 550, anchor="nw", window=button5)

#Adding Input boxes to canvas
e1_window = Canvas1.create_window(200,300,anchor="nw",window=e1)
e2_window = Canvas1.create_window(170,450,anchor="nw",window=e2)
e3_window = Canvas1.create_window(950,450,anchor="nw",window=e3)
root.mainloop()