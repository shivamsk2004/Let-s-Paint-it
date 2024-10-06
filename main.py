from tkinter import*

root=Tk()
root.title("Let's Paint")
root.geometry("1100x600")

frame1 = Frame(root,height=100,width=1100,bg="red")
frame1.grid(row=0,column=0,sticky=NW)

toolsFrame = Frame(frame1, height=100, width=100, bg="green")
toolsFrame.grid(row=0,column=0)

pencilButton=Button(toolsFrame,text="Pencil",width=10)
pencilButton.grid(row=0,column=0)

eraserButton=Button(toolsFrame,text="Eraser",width=10)
eraserButton.grid(row=1,column=0)

toolsLabel=Label(toolsFrame,text="Tools",width=10)
toolsLabel.grid(row=2,column=0)
#tkinter mein rows,columns by default 0 se start hoti hai
#frames matlab alag alag blocks
frame2 = Frame(root,height=500,width=1100,bg="yellow")
frame2.grid(row=1,column=0)

canvas=Canvas(frame2, height=500, width=1100, bg="white")
canvas.grid(row=0,column=0)

#canvas.create_line(100,100,200,200)
#canvas.create_oval(100,100,120,120,fill="black")
#basically line from (x,y) to (x',y')

#variables for pencil

prevPoint = [0,0]
currentPoint = [0,0]
def paint(event):
    global prevPoint
    global currentPoint
    x=event.x
    y=event.y
    currentPoint = [x,y]
    #canvas.create_oval(x,y,x+2,y+2,fill="black")
    if prevPoint!= [0,0] : #ab top left corner se start nhi hoga
        canvas.create_line(prevPoint[0],prevPoint[1],currentPoint[0],currentPoint[1])

    prevPoint=currentPoint

    if event.type == "5" : #ye terminal se samajh aaya ki line nikalo toh 
        prevPoint=[0,0]    #6 number hota hai, agar chod do toh 5 ho jata hai
        
canvas.bind("<B1-Motion>",paint)
canvas.bind("<ButtonRelease-1>",paint)
#canvas.bind("<Button-1>",paint)
#mouse ke left button ke saath connect hogaya hai

root.resizable(False,False) #we don't need to resize height as well width
root.mainloop()
