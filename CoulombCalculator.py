from tkinter import *
import os
import pathlib

#Current Path script is in
currentPath = pathlib.Path(__file__).parent.resolve()

###################
Window = Tk()
print("")

#App Geometry
Window.geometry("400x400")
Window.title("Coulomb Calculator")

#App Icon
imgicon = PhotoImage(file=os.path.join(currentPath,'Physics.png'))
Window.tk.call('wm', 'iconphoto', Window._w, imgicon)  

#####################

#Calculate Force
def calculateForce():
    #F = K(q1q2/r^2)
    q1 = float(chargeOneEntry.get())
    q2 = float(chargeTwoEntry.get())
    r = float(distanceEntry.get())
    k = (8.99*(10**9))

    Force = (k*( ((q1)*(10**-6))*((q2)*(10**-6))/(r**2) ))
    
    forceOutput = Label(Window, text = Force)
    canvasOne.create_window(200,250, window = forceOutput)

    unitLabel = Label(Window, text = "Force in Newtons")
    canvasOne.create_window(200,230, window = unitLabel)

    return Force

def copyToo():
    Tk.clipboard_clear(Window)
    Tk.clipboard_append(Window, calculateForce())

#####################

#Canvas
canvasOne = Canvas(Window, width = 400, height = 300)
canvasOne.pack()

#Labels
chargeOneLabel = Label(Window, text = "q1")
canvasOne.create_window(15,60, window = chargeOneLabel)

chargeTwoLabel = Label(Window, text = "q2")
canvasOne.create_window(15,100, window = chargeTwoLabel)

distanceLabel = Label(Window, text = "r")
canvasOne.create_window(15,140, window = distanceLabel)

#-

chargeOneUnitLabel = Label(Window, text = "Assumes µC")
canvasOne.create_window(90,40, window = chargeOneUnitLabel)

chargeTwoUnitLabel = Label(Window, text = "Assumes µC")
canvasOne.create_window(90,80, window = chargeTwoUnitLabel)

distanceUnitLabel = Label(Window, text = "Assumes Meters")
canvasOne.create_window(90,120, window = distanceUnitLabel)

###################

#Input/Entry Fields
chargeOneEntry = Entry(Window)
canvasOne.create_window(90,60, window = chargeOneEntry)

chargeTwoEntry = Entry(Window)
canvasOne.create_window(90,100, window = chargeTwoEntry)

distanceEntry = Entry(Window)
canvasOne.create_window(90,140, window = distanceEntry)

#Output

findButton = Button(Window, text = "Calculate", command = calculateForce)
canvasOne.create_window(55,250, window = findButton)

copyButton = Button(Window, text = "Copy", command = copyToo)
canvasOne.create_window(42,300, window = copyButton)

######################
Window.resizable(False, False)
Window.mainloop()