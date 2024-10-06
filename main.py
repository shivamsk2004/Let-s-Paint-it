from tkinter import*

root=Tk()
root.title("Let's Paint")
root.geometry("1100x600")

frame1 = Frame(root,height=100,width=1100,bg="red")
frame1.grid(row=0,column=0)
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
        
canvas.bind("<B1-Motion>",paint)
#canvas.bind("<Button-1>",paint)
#mouse ke left button ke saath connect hogaya hai

root.resizable(False,False) #we don't need to resize height as well width
root.mainloop()
