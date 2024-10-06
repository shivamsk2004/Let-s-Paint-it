from tkinter import*
from tkinter import colorchooser
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog
from tkinter import messagebox

root=Tk()
root.title("Let's Paint")
root.geometry("1100x600")

frame1 = Frame(root,height=100,width=1100)
frame1.grid(row=0,column=0,sticky=NW)
#toolsFrame
toolsFrame = Frame(frame1, height=100, width=100)
toolsFrame.grid(row=0,column=0)

def usePencil():
    stroke_color.set("black")
    canvas["cursor"]="arrow"
def useEraser():
    stroke_color.set("white")
    canvas["cursor"]=DOTBOX

pencilButton=Button(toolsFrame,text="Pencil",width=10,command=usePencil)
pencilButton.grid(row=0,column=0)

eraserButton=Button(toolsFrame,text="Eraser",width=10,command=useEraser)
eraserButton.grid(row=1,column=0)

toolsLabel=Label(toolsFrame,text="Tools",width=10)
toolsLabel.grid(row=2,column=0)

#sizeFrame
sizeFrame=Frame(frame1,height=100,width=100)
sizeFrame.grid(row=0,column=1)

defaultButton = Button(sizeFrame,text="Default",width=10,command=usePencil)
defaultButton.grid(row=0,column=0)

stroke_size = IntVar()
stroke_size.set(1)
options = [1,2,3,4,5]

sizeList=OptionMenu(sizeFrame,stroke_size,*options)
sizeList.grid(row=1,column=0)

sizeLabel=Label(sizeFrame,text="Size",width=10)
sizeLabel.grid(row=2,column=0)

stroke_color=StringVar()
stroke_color.set("black")

#colorBoxFrame
colorBoxFrame=Frame(frame1,height=100,width=100,relief=SUNKEN,borderwidth=3)
colorBoxFrame.grid(row=0,column=2)

previousColor=StringVar()
previousColor.set("white")
previousColor2=StringVar()
previousColor2.set("white")

def selectColor():
    selectedColor=colorchooser.askcolor("blue",title="Select Color")
    if selectedColor[1]==None:
        stroke_color.set("black") 
    else:
        stroke_color.set(selectedColor[1])
        previousColor2.set(previousColor.get())
        previousColor.set(selectedColor[1])
       
        previousColorButton["bg"]=previousColor.get()
        previousColor2Button["bg"]=previousColor2.get()

colorBoxButton=Button(colorBoxFrame,text="Select Color",width=10,command=selectColor)
colorBoxButton.grid(row=0,column=0)

previousColorButton=Button(colorBoxFrame,text="Previous",width=10,command=lambda:stroke_color.set(previousColor.get()))
previousColorButton.grid(row=1,column=0)

previousColor2Button=Button(colorBoxFrame,text="Previous2",width=10,command=lambda:stroke_color.set(previousColor2.get()))
previousColor2Button.grid(row=2,column=0)

#saveImageFrame
def saveImage():
    try:
        fileLocation=filedialog.asksaveasfilename(defaultextension="jpg")
        x=root.winfo_rootx()
        y=root.winfo_rooty()+110
        img=ImageGrab.grab(bbox=(x,y,x+1100,y+500))
        img.save(fileLocation)
        showImage=messagebox.askyesno("Let's Paint it","Do you want to open image?")
        print(showImage)
        if showImage:
            img.show()
    except  Exception as e:
        messagebox.showinfo("Let's Paint it:","Error Occured")

def clear():
    if messagebox.askokcancel("Let's Paint it","Do you want to clear everything"):
       canvas.delete('all')

def createNew():
    if messagebox.askyesno("Let's Paint it","Do you want to save before you clear everything?"):
        saveImage()
saveImageFrame=Frame(frame1,height=100,width=100,relief=SUNKEN,borderwidth=3)
saveImageFrame.grid(row=0,column=4)

saveImageButton=Button(saveImageFrame,text="Save",bg="white",width=10,command=saveImage)
saveImageButton.grid(row=0,column=0)
newImageButton=Button(saveImageFrame,text="New",bg="white",width=10,command=createNew)
newImageButton.grid(row=1,column=0)
clearImageButton=Button(saveImageFrame,text="Clear",bg="white",width=10,command=clear)
clearImageButton.grid(row=2,column=0)

#helpSettingFrame
def help():
    messagebox.showinfo("Help","1.Click on {Select Color} Option selcect specific color\n2.Click on {Clear} to clear entire Canvas")
def settings():
    messagebox.showwarning("Settings","Not Available") 
def about():
    messagebox.showinfo("About","User-Friendly Paint App")
helpSettingFrame=Frame(frame1,height=100,width=100,relief=SUNKEN,borderwidth=3)
helpSettingFrame.grid(row=0,column=5)

helpButton=Button(helpSettingFrame,text="Help",bg="white",width=10,command=help)
helpButton.grid(row=0,column=0)
settingButton=Button(helpSettingFrame,text="Settings",bg="white",width=10,command=settings)
settingButton.grid(row=1,column=0)
aboutButton=Button(helpSettingFrame,text="About",bg="white",width=10,command=about)
aboutButton.grid(row=2,column=0)

#colorsFrame
colorsFrame=Frame(frame1,height=100,width=100,relief=SUNKEN,borderwidth=3)
colorsFrame.grid(row=0,column=3)

redButton=Button(colorsFrame,text="Red",bg="red",width=10,command=lambda:stroke_color.set("red"))
redButton.grid(row=0,column=0)

greenButton=Button(colorsFrame,text="Green",bg="green",width=10,command=lambda:stroke_color.set("green"))
greenButton.grid(row=1,column=0)

blueButton=Button(colorsFrame,text="Blue",bg="blue",width=10,command=lambda:stroke_color.set("blue"))
blueButton.grid(row=2,column=0)

purpleButton=Button(colorsFrame,text="Purple",bg="purple",width=10,command=lambda:stroke_color.set("purple"))
purpleButton.grid(row=0,column=1)

yellowButton=Button(colorsFrame,text="Yellow",bg="yellow",width=10,command=lambda:stroke_color.set("yellow"))
yellowButton.grid(row=1,column=1)

orangeButton=Button(colorsFrame,text="Orange",bg="orange",width=10,command=lambda:stroke_color.set("orange"))
orangeButton.grid(row=2,column=1)
#tkinter mein rows,columns by default 0 se start hoti hai
#frames matlab alag alag blocks
frame2 = Frame(root,height=500,width=1100,bg="yellow")
frame2.grid(row=1,column=0)

canvas=Canvas(frame2,height=500,width=1100,bg="white")
canvas.grid(row=0,column=0)
#canvas.create_line(100,100,200,200)
#canvas.create_oval(100,100,120,120,fill="black")
#basically line from (x,y) to (x',y')
#variables for pencil

prevPoint = [0,0]
currentPoint = [0,0]
def paintRight(event):
    x=event.x
    y=event.y
    canvas.create_arc(x,y,x+stroke_size.get(),y+stroke_size.get(),fill=stroke_color.get(),outline=stroke_color.get(),width=stroke_size.get())

def paint(event):
    global prevPoint
    global currentPoint
    x=event.x
    y=event.y
    currentPoint = [x,y]
    #canvas.create_oval(x,y,x+2,y+2,fill="black")
    if prevPoint!= [0,0] : #ab top left corner se start nhi hoga
        canvas.create_polygon(prevPoint[0],prevPoint[1],currentPoint[0],currentPoint[1],fill=stroke_color.get(),outline=stroke_color.get(),width=stroke_size.get())

    prevPoint=currentPoint

    if event.type == "5" : #ye terminal se samajh aaya ki line nikalo toh 
        prevPoint=[0,0]    #6 number hota hai, agar chod do toh 5 ho jata hai
        
canvas.bind("<B1-Motion>",paint)
canvas.bind("<ButtonRelease-1>",paint)
canvas.bind("<B3-Motion>",paintRight)
#B-3 is used for the right button
#canvas.bind("<Button-1>",paint)
#mouse ke left button ke saath connect hogaya hai

root.resizable(False,False) #we don't need to resize height as well width
root.mainloop()
