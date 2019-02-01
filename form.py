from tkinter import *

screen=Tk()
screen.geometry("500x500")
screen.title("Python Form")
heading=Label(text="Python Form",bg="grey",fg="black",width="500",height="3")
heading.pack()

x_coord=Label(text="X Coordinate",)
y_coord=Label(text="Y Coordinate",)
theta1=Label(text="θ1",)
theta3=Label(text="θ3",)
theta4=Label(text="θ4",)

x_coord.place(x=15,y=70)
y_coord.place(x=15,y=140)
theta1.place(x=15,y=210)
theta3.place(x=15,y=280)
theta4.place(x=15,y=350)

xcoord= StringVar()
ycoord= StringVar()
t1= StringVar()
t2= StringVar()
t3= StringVar()

x_coord_entry=Entry(textvariable=xcoord,width="30")
y_coord_entry=Entry(textvariable=ycoord,width="30")
theta1_entry=Entry(textvariable=t1,width="30")
theta3_entry=Entry(textvariable=t2,width="30")
theta4_entry=Entry(textvariable=t3,width="30")

x_coord_entry.place(x=15,y=100)
y_coord_entry.place(x=15,y=180)
theta1_entry.place(x=15,y=240)
theta3_entry.place(x=15,y=300)
theta4_entry.place(x=15,y=360)
